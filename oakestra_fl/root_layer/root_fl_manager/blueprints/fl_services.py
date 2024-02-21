from http import HTTPStatus

import flask
import flask_openapi3
from image_registry.main import latest_image_already_exists
from utils.general import GITHUB_PREFIX

fl_services_blp = flask_openapi3.APIBlueprint(
    "fl-services",
    __name__,
    url_prefix="/api/fl-services",
)


@fl_services_blp.post("/")
def post_fl_service():
    data = flask.request.json
    repo_url = data["code"]

    if not repo_url.startswith(GITHUB_PREFIX):
        return {
            "message": "Please provide the code in the form of a valid GitHub repository."
        }, HTTPStatus.BAD_REQUEST

    repo_name = repo_url.split(GITHUB_PREFIX)[-1]

    status, image_exists = latest_image_already_exists(repo_name)
    if status != HTTPStatus.OK:
        return status
    if image_exists:
        return {
            "message": "The lastest image based on the provided repo already exists."
        }, HTTPStatus.OK

    # build_and_push_image()

    # push_image_to_root_registry()

    return {"message": "FL service has been properly prepared"}, HTTPStatus.OK
