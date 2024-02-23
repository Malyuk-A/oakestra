import os
from http import HTTPStatus

import blueprints as blps
import flask_openapi3
from utils.certificate_generator import handle_certificate

ROOT_MQTT_BROKER_URL = os.environ.get("ROOT_MQTT_BROKER_URL")
ROOT_MQTT_BROKER_PORT = os.environ.get("ROOT_MQTT_BROKER_PORT")

ROOT_FL_MANAGER_PORT = os.environ.get("ROOT_FL_MANAGER_PORT")

info = flask_openapi3.Info(title="Root FL Manager API", version="1.0.0")
app = flask_openapi3.OpenAPI(__name__, info=info)


@app.route("/", methods=["GET"])
def health():
    return {"message": "ok"}, HTTPStatus.OK


def main():
    handle_certificate()

    # for blp in blps.blueprints:
    #     app.register_api(blp)

    # app.run(
    #     host="0.0.0.0",
    #     port=ROOT_FL_MANAGER_PORT,
    #     debug=False,
    # )

    import paho.mqtt.client as paho_mqtt

    # Define the callback function
    def on_message(client, userdata, message):
        # Print the message payload

        app.logger.info(f"Received message: {message.payload.decode()}")

        # Run some code based on the message
        # For example, print "Hello" if the message is "Hi"
        if message.payload.decode() == "Hi":
            app.logger.info("Hello")

    # Create a client object
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    # Assign the callback function
    mqtt_client.on_message = on_message
    # Connect to the broker
    mqtt_client.connect(ROOT_MQTT_BROKER_URL, int(ROOT_MQTT_BROKER_PORT))
    app.logger.info(f"ROOT_MQTT_BROKER_URL = {ROOT_MQTT_BROKER_URL}")
    app.logger.info(f"ROOT_MQTT_BROKER_PORT = {ROOT_MQTT_BROKER_PORT}")
    # Subscribe to the topic "test"
    mqtt_client.subscribe("test")
    # Loop forever to keep the connection alive
    app.logger.info("AAAAAAAAAAAA")
    mqtt_client.loop_forever()


if __name__ == "__main__":
    main()
