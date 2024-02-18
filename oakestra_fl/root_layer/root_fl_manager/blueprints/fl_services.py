import flask
import flask_openapi3

fl_services_blp = flask_openapi3.APIBlueprint(
    "fl-services",
    __name__,
    url_prefix="/api/fl-services",
)


@fl_services_blp.post("/")
def post_fl_service():
    from root_fl_manager import app

    app.logger.error("AAAAAAAAAAA")
    app.logger.warning("BBBBBBBBBB")
    app.logger.info("CCCCCCCCCCC")
    app.logger.debug("DDDDDDDDDDDD")

    data = flask.request.json

    app.logger.error("chaooooooooooo")

    print(data)
    app.logger.debug(f"data = {data}")
    return {"message": "FL service has been properly prepared"}, 200
