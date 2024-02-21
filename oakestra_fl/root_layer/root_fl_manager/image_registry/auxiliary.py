from http import HTTPStatus
from typing import Any, List, Optional, Tuple

from utils.general import ROOT_FL_IMAGE_REGISTRY_PORT, send_github_request, send_request
from utils.logging import logger

# TODO figure out an automatic way to get the real public IP of the host (or another nicer solution)
ROOT_FL_IMAGE_REGISTRY_NAME = "192.168.178.44"
FULL_ROOT_FL_IMAGE_REGISTRY_NAME = f"{ROOT_FL_IMAGE_REGISTRY_NAME}:{ROOT_FL_IMAGE_REGISTRY_PORT}"

ROOT_FL_IMAGE_REGISTRY_URL = f"https://{FULL_ROOT_FL_IMAGE_REGISTRY_NAME}"


def send_reqistry_request(api_endpoint: str = None) -> Tuple[HTTPStatus, Optional[Any]]:
    return send_request(ROOT_FL_IMAGE_REGISTRY_URL, api_endpoint, "Root Image Registry")


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


def get_latest_commit_hash(repo_name: str) -> Tuple[HTTPStatus, Optional[str]]:

    core_git_api_endpoint = f"/repos/{repo_name}/commits"
    main_git_api_enpoint = f"{core_git_api_endpoint}/main"

    status, json_data = send_github_request(main_git_api_enpoint)
    if status != HTTPStatus.OK:
        return status, None

    # Note: Cut down the long hash to the usual short one for readability.
    return status, json_data["sha"][:7]
