import json
import os

import paho.mqtt.client as paho_mqtt
from api.common import GITHUB_PREFIX
from fl_services.main import handle_new_fl_service
from utils.logging import logger

ROOT_MQTT_BROKER_URL = os.environ.get("ROOT_MQTT_BROKER_URL")
ROOT_MQTT_BROKER_PORT = os.environ.get("ROOT_MQTT_BROKER_PORT")


def on_new_service_message(client, userdata, message):
    decoded_message = message.payload.decode()
    logger.debug(f"Received message: {decoded_message}")
    data = json.loads(decoded_message)
    if data["virtualization"] == "ml-repo" and data["code"].startswith(GITHUB_PREFIX):
        handle_new_fl_service(data)


def handle_mqtt():
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.on_message = on_new_service_message
    mqtt_client.connect(ROOT_MQTT_BROKER_URL, int(ROOT_MQTT_BROKER_PORT))
    mqtt_client.subscribe("new/services")
    mqtt_client.loop_forever()
