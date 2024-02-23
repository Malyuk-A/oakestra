from http import HTTPStatus
from typing import Optional, Tuple

from image_registry.auxiliary import (
    FULL_ROOT_FL_IMAGE_REGISTRY_NAME,
    check_registry_reachable,
    get_current_registry_image_repos,
    get_current_registry_repo_image_tags,
    get_latest_commit_hash,
)
from utils.general import docker
from utils.logging import logger


def latest_image_already_exists(repo_name: str) -> Tuple[HTTPStatus, Optional[str]]:
    status, current_images_repos = get_current_registry_image_repos()
    if status != HTTPStatus.OK or repo_name not in current_images_repos:
        return status, None

    status, current_image_repo_tags = get_current_registry_repo_image_tags(repo_name)
    if status != HTTPStatus.OK:
        return status, None
    status, latest_commit_hash = get_latest_commit_hash(repo_name)
    if status != HTTPStatus.OK:
        return status, None

    if latest_commit_hash in current_image_repo_tags:
        return status, f"{repo_name}:{latest_commit_hash}"
    else:
        return status, None


def push_image_to_root_registry():
    status = check_registry_reachable()
    if status != HTTPStatus.OK:
        return status

    pulled_image_name = "alpine:latest"
    docker.images.pull(pulled_image_name)

    # new_image_name = f"{EXTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME}/alpinum:latest-testalex6"
    # new_image_name = "192.168.178.44:5073/alpinum:latest-testalex7"
    new_image_name = f"{FULL_ROOT_FL_IMAGE_REGISTRY_NAME}/alpinum3:latest"

    docker.images.get(pulled_image_name).tag(new_image_name)

    docker.images.push(new_image_name)

    logger.info(get_current_registry_image_repos())
