from http import HTTPStatus
from typing import Any, Optional, Tuple

from api.utils import send_github_request, send_request
from image_registry.common import ROOT_FL_IMAGE_REGISTRY_URL


def send_reqistry_request(api_endpoint: str = None) -> Tuple[HTTPStatus, Optional[Any]]:
    return send_request(ROOT_FL_IMAGE_REGISTRY_URL, api_endpoint, "Root Image Registry")


def get_latest_commit_hash(repo_name: str) -> Tuple[HTTPStatus, Optional[str]]:

    core_git_api_endpoint = f"/repos/{repo_name}/commits"
    main_git_api_enpoint = f"{core_git_api_endpoint}/main"

    status, json_data = send_github_request(main_git_api_enpoint)
    if status != HTTPStatus.OK:
        return status, None

    # Note: Cut down the long hash to the usual short one for readability.
    return status, json_data["sha"][:7]
