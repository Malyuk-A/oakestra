import os

import flask_openapi3
from blueprints import blueprints

ROOT_FL_MANAGER_PORT = os.environ.get("ROOT_FL_MANAGER_PORT")

info = flask_openapi3.Info(title="Root FL Manager API", version="1.0.0")
app = flask_openapi3.OpenAPI(__name__, info=info)


@app.route("/", methods=["GET"])
def health():
    app.logger.error("error")
    app.logger.warning("warning")
    app.logger.info("info")
    app.logger.debug("debug")
    return {"message": "Ok"}, 200


def main():
    for blp in blueprints:
        app.register_api(blp)

    app.logger.info(ROOT_FL_MANAGER_PORT)

    app.run(
        host="0.0.0.0",
        # port=ROOT_FL_MANAGER_PORT, <- FIX !!!! iNVESTIGATE WHY & HOW THIS IS NOT WORKING ? (easiest reason typo or so)
        # TODO NEXST REAL STEP IN OAKESTRA FL
        # FIX root fl manager - check why os env var not working
        # then check if system-manager can now reach it properly
        # then check post
        # if post works - do the registry thingy with the image building pipeline
        port=5072,
        debug=False,
    )


if __name__ == "__main__":
    main()
