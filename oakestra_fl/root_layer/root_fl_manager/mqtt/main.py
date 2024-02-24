import os

import paho.mqtt.client as paho_mqtt
from utils.logging import normal_logger

ROOT_MQTT_BROKER_URL = os.environ.get("ROOT_MQTT_BROKER_URL")
ROOT_MQTT_BROKER_PORT = os.environ.get("ROOT_MQTT_BROKER_PORT")


def on_message(client, userdata, message):
    normal_logger.info(f"Received message: {message.payload.decode()}")
    if message.payload.decode() == "Hi":
        normal_logger.info("Hello")

    normal_logger.info("haha")
    normal_logger.info(f"client = '{client}'")
    normal_logger.info(f"userdata = '{userdata}'")
    normal_logger.info(f"message = '{message}'")


def handle_mqtt():
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.on_message = on_message
    mqtt_client.connect(ROOT_MQTT_BROKER_URL, int(ROOT_MQTT_BROKER_PORT))
    mqtt_client.subscribe("new/services")
    mqtt_client.loop_forever()
