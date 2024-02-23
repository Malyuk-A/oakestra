import os

import paho.mqtt.client as paho_mqtt

ROOT_MQTT_BROKER_URL = os.environ.get("ROOT_MQTT_BROKER_URL")
ROOT_MQTT_BROKER_PORT = os.environ.get("ROOT_MQTT_BROKER_PORT")

mqtt_client = None


def handle_mqtt():
    global mqtt_client
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.connect(ROOT_MQTT_BROKER_URL, int(ROOT_MQTT_BROKER_PORT))
    mqtt_client.publish("test", "Hello from Python")
