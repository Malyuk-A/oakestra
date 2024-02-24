from http import HTTPStatus
from typing import Dict

from api.common import GITHUB_PREFIX
from image_builder_management.main import delegate_image_build
from image_registry.main import latest_image_already_exists
from utils.logging import logger


def handle_new_fl_service(new_fl_service: Dict) -> None:
    service_id = new_fl_service["microserviceID"]
    repo_url = new_fl_service["code"]
    repo_name = repo_url.split(GITHUB_PREFIX)[-1]

    status, existing_image_name = latest_image_already_exists(repo_name)
    if status != HTTPStatus.OK:
        logger.critical(f"Failed to check latest image based on this repo name: '{repo_name}'")
        return

    if existing_image_name is not None:
        # TODO update_service_image(new_fl_service, existing_image_name)
        # TODO logger.info(f"FL service '{service_id}' has been properly prepared")
        return

    delegate_image_build(service_id, repo_url)
