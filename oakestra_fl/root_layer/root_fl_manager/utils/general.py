import os
from http import HTTPStatus
from typing import Any, Optional, Tuple

# Note: Instead of using python-on-whales the more mature docker SDK python lib
# should not require/install the docker CLI to work.
import docker as docker_sdk
import requests

ROOT_FL_IMAGE_REGISTRY_DNS_NAME = "root_fl_image_registry"
ROOT_FL_IMAGE_REGISTRY_PORT = os.environ.get("ROOT_FL_IMAGE_REGISTRY_PORT")

SYSTEM_MANAGER_IP = os.environ.get("SYSTEM_MANAGER_IP")
SYSTEM_MANAGER_PORT = os.environ.get("SYSTEM_MANAGER_PORT")
SYSTEM_MANAGER_URL = f"http://{SYSTEM_MANAGER_IP}:{SYSTEM_MANAGER_PORT}"

GITHUB_PREFIX = "https://github.com/"

docker = docker_sdk.from_env()


def send_request(
    base_url: str, api_endpoint: str = None, error_msg_subject: str = None
) -> Tuple[HTTPStatus, Optional[Any]]:
    url = base_url
    if api_endpoint is not None:
        url = f"{base_url}{api_endpoint}"

    try:
        response = requests.get(url, verify=False)
        response_status = HTTPStatus(response.status_code)
        if response_status == HTTPStatus.OK:
            return response_status, response.json()
        else:
            return (
                response_status,
                f"{error_msg_subject} request failed with '{response_status}' for '{url}",
            )
    except requests.exceptions.RequestException as e:
        return (
            HTTPStatus.INTERNAL_SERVER_ERROR,
            f"{error_msg_subject} request failed with '{e}' for '{url}",
        )


def send_github_request(api_endpoint: str = None) -> Tuple[HTTPStatus, Optional[Any]]:
    return send_request("https://api.github.com", api_endpoint, "Github")
