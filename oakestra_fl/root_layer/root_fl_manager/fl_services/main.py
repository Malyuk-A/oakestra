from http import HTTPStatus
from typing import Dict

from image_builder_management.main import delegate_image_build, undeploy_builder_app
from image_builder_management.repo_management import MlRepo
from image_registry.main import latest_image_already_exists
from utils.logging import logger


def handle_new_fl_service(new_fl_service: Dict) -> None:
    service_id = new_fl_service["microserviceID"]
    ml_repo = MlRepo(new_fl_service["code"])

    status, existing_image_name = latest_image_already_exists(ml_repo)

    if status != HTTPStatus.OK:
        logger.critical(f"Failed to check latest image based on this repo name: '{ml_repo.name}'")
        return

    if existing_image_name is not None:
        # TODO update_service_image(new_fl_service, existing_image_name)
        # TODO logger.info(f"FL service '{service_id}' has been properly prepared")
        return

    delegate_image_build(service_id, ml_repo)


def handle_builder_success(builder_sucess_msg: Dict) -> None:
    origin_fl_service_id = builder_sucess_msg["service_id"]
    image_name_with_tag = builder_sucess_msg["image_name_with_tag"]
    builder_app_name = builder_sucess_msg["builder_app_name"]

    undeploy_builder_app(builder_app_name)
