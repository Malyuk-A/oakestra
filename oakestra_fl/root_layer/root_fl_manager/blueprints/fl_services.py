import flask
import flask_openapi3
from image_registry.main import latest_image_already_exists
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

    if not repo_url.startswith(GITHUB_PREFIX):
        return {"message": "Please provide the code in the form of a valid GitHub repository."}, 400

    repo_name = repo_url.split(GITHUB_PREFIX)[-1]

    if latest_image_already_exists(repo_name):
        return {"message": "The lastest image based on the provided repo already exists."}, 200

    # build_and_push_image()

    # push_image_to_root_registry()

    return {"message": "FL service has been properly prepared"}, 200
