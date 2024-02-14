import os

from api.v1 import blueprints
from flask import Flask
from flask_smorest import Api
from flask_swagger_ui import get_swaggerui_blueprint

FL_ROOT_MANAGER_PORT = os.environ.get("FL_ROOT_MANAGER_PORT")

app = Flask(__name__)

app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["API_TITLE"] = "FL Root Manager Api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_URL_PREFIX"] = "/docs"

api = Api(app)

SWAGGER_URL = "/api/docs"
API_URL = "/docs/openapi.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "FL Root Manager"},
)
app.register_blueprint(swaggerui_blueprint)

# for blp in blueprints:
#     api.register_blueprint(blp)


@app.route("/", methods=["GET"])
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FL_ROOT_MANAGER_PORT, debug=False)
