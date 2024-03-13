from http import HTTPStatus
from typing import List, Optional, Tuple

from image_registry.utils import get_latest_commit_hash, send_reqistry_request


def check_registry_reachable() -> HTTPStatus:
    status, _ = send_reqistry_request()
    return status


# Note: (image) repos are the "grouping" of all tags of a single image.
# E.g. The (image) repo "alpine" can have multiple tags "latest", "1.0.0", etc.
# We usually first check the image repo and then its tags.
def get_current_registry_image_repos() -> Tuple[HTTPStatus, Optional[List[str]]]:
    status, json_data = send_reqistry_request("/v2/_catalog")
    if status != HTTPStatus.OK:
        return status, None
    return status, json_data["repositories"]


def get_current_registry_repo_image_tags(repo_name: str) -> Tuple[HTTPStatus, Optional[List[str]]]:
    status, json_data = send_reqistry_request(f"/v2/{repo_name}/tags/list")
    if status != HTTPStatus.OK:
        return status, None
    return status, json_data["tags"]


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
