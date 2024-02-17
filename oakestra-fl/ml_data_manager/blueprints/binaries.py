import flask
import flask_openapi3

binaries_blp = flask_openapi3.APIBlueprint(
    "binairies",
    __name__,
    url_prefix="/binaries",
)


@binaries_blp.post("/")
def post_binary_data():
    # Check if the request has the required content type
    if flask.request.headers.get("Content-Type") != "application/octet-stream":
        return {"error": "Bad request"}, 400

    # Get the binary data from the request
    binary_data = flask.request.data

    # Write the binary data to a file
    with open("binary_data.bin", "wb") as file:
        file.write(binary_data)

    return {"message": "Data posted successfully"}, 200
