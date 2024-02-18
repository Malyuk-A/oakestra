import os

import flask_openapi3
from blueprints import blueprints

ROOT_FL_MANAGER_PORT = os.environ.get("ROOT_FL_MANAGER_PORT")

info = flask_openapi3.Info(title="Root FL Manager API", version="1.0.0")
app = flask_openapi3.OpenAPI(__name__, info=info)


@app.route("/", methods=["GET"])
def health():
    return {"message": "Ok"}, 200


def main():
    for blp in blueprints:
        app.register_api(blp)

    app.run(
        host="0.0.0.0",
        port=ROOT_FL_MANAGER_PORT,
        debug=True,
    )


if __name__ == "__main__":
    main()
