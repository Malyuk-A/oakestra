import flask
import flask_openapi3
from image_registry.main import push_image_to_root_registry
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

    if not repo_url.startswith("https://github.com/"):
        return {"message": "Please provide the code in the form of a valid GitHub repository."}, 400

    repo_name = repo_url.split("://")[-1]

    push_image_to_root_registry()

    return {"message": "FL service has been properly prepared"}, 200
