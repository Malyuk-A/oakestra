import os

import flask_openapi3

import ml_data_manager.

ML_DATA_MANAGER_PORT = os.environ.get("ML_DATA_MANAGER_PORT")

info = flask_openapi3.Info(title="ML Data Manager API", version="1.0.0")
app = flask_openapi3.OpenAPI(__name__, info=info)


@app.route("/", methods=["GET"])
def health():
    return {"message": "Ok"}, 200


def main():
    for blp in blueprints:
        app.register_api(blp)

    app.run(host="0.0.0.0", port=ML_DATA_MANAGER_PORT, debug=True)


if __name__ == "__main__":
    main()
