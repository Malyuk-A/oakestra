import os

import paho.mqtt.client as paho_mqtt

ROOT_MQTT_BROKER_URL = os.environ.get("ROOT_MQTT_BROKER_URL")
ROOT_MQTT_BROKER_PORT = os.environ.get("ROOT_MQTT_BROKER_PORT")

mqtt_client = None


def init_mqtt() -> paho_mqtt.Client:
    global mqtt_client
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.connect(ROOT_MQTT_BROKER_URL, int(ROOT_MQTT_BROKER_PORT))
    return mqtt_client


def get_mqtt_client():
    if mqtt_client is None:
        return init_mqtt()
    else:
        return mqtt_client
