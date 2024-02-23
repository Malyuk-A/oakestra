from http import HTTPStatus

import flask
import flask_openapi3
from image_registry.main import latest_image_already_exists
from services.main import update_service_image
from utils.general import GITHUB_PREFIX
from utils.logging import logger

fl_services_blp = flask_openapi3.APIBlueprint(
    "fl-services",
    __name__,
    url_prefix="/api/fl-services",
)


@fl_services_blp.post("/")
def post_fl_service():
    data = flask.request.json
    repo_url = data["code"]

    # logger.debug("A#" * 10)
    # logger.debug(data)
    # logger.debug("a-" * 10)
    update_service_image(data, "alextesting")
    exit(0)

    if not repo_url.startswith(GITHUB_PREFIX):
        return {
            "message": "Please provide the code in the form of a valid GitHub repository."
        }, HTTPStatus.BAD_REQUEST

    repo_name = repo_url.split(GITHUB_PREFIX)[-1]

    status, existing_image_name = latest_image_already_exists(repo_name)
    if status != HTTPStatus.OK:
        return status
    if existing_image_name is not None:
        update_service_image(data, existing_image_name)
        return (
            {
                "message": """The lastest image based on the provided repo already exists.
            The """
            },
            HTTPStatus.OK,
        )

    # TODO delegate_image_build_and_push()

    return {"message": "FL service has been properly prepared"}, HTTPStatus.OK
