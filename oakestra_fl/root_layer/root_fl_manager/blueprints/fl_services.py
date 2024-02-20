import flask
import flask_openapi3
from root_fl_manager import app

fl_services_blp = flask_openapi3.APIBlueprint(
    "fl-services",
    __name__,
    url_prefix="/api/fl-services",
)


@fl_services_blp.post("/")
def post_fl_service():
    data = flask.request.json
    repo_url = data["code"]

    if not repo_url.srtartswith("https://github.com/"):
        return {"message": "Please provide the code in the form of a valid GitHub repository."}, 400

    repo_name = repo_url.split("://")[-1]

    return {"message": "FL service has been properly prepared"}, 200
