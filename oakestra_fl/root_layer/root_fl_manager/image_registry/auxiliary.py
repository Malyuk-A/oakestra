from typing import Any, List

import requests
from utils.general import ROOT_FL_IMAGE_REGISTRY_DNS_NAME, ROOT_FL_IMAGE_REGISTRY_PORT, docker
from utils.logging import logger

INTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME = (
    f"{ROOT_FL_IMAGE_REGISTRY_DNS_NAME}:{ROOT_FL_IMAGE_REGISTRY_PORT}"
)
# TODO figure out an automatic way to get the real public IP of the host (or another nicer solution)
ROOT_FL_IMAGE_REGISTRY_NAME = "192.168.178.44"
FULL_ROOT_FL_IMAGE_REGISTRY_NAME = f"{ROOT_FL_IMAGE_REGISTRY_NAME}:{ROOT_FL_IMAGE_REGISTRY_PORT}"

ROOT_FL_IMAGE_REGISTRY_URL = f"https://{INTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME}"


def check_registry_reachable(repo_name: str) -> bool:
    try:
        response = requests.get(ROOT_FL_IMAGE_REGISTRY_URL, verify=False)
        if response.status_code == 200:
            return True
        else:
            logger.error(
                f"Root Image Registry is not reachable. Status code: {response.status_code}"
            )
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Error reaching the registry: {e}")
        return False


def get_current_registry_images() -> List[Any]:
    return docker.images.list(filters={"reference": ROOT_FL_IMAGE_REGISTRY_URL})


def get_latest_commit_hash(repo_name: str) -> str:
    core_git_api_url = f"https://api.github.com/repos/{repo_name}/commits"
    main_git_api_url = f"{core_git_api_url}/main"
    respone = requests.get(main_git_api_url)
    data = respone.json()
    # Note: Cut down the long hash to the usual short one for readability.
    return data["sha"][:7]
