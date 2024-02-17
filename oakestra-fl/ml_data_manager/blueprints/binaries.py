import pathlib
from datetime import datetime

import flask
import flask_openapi3

CONTENT_TYPE = "application/octet-stream"
ML_DATA_VOLUME = pathlib.Path("ml_data_volume")

binaries_blp = flask_openapi3.APIBlueprint(
    "binaries",
    __name__,
    url_prefix="/api/data/binaries",
)


@binaries_blp.post("/")
def post_binary_data():

    if flask.request.headers.get("Content-Type") != CONTENT_TYPE:
        return {"error": f"Bad request, the Header Content-Type should be '{CONTENT_TYPE}'"}, 400

    # Get the binary data from the request
    binary_data = flask.request.data

    # Write the binary data to a file
    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
    with open(f"{ML_DATA_VOLUME / current_time}.bin", "wb") as file:
        file.write(binary_data)

    return {"message": "Data posted successfully"}, 200
