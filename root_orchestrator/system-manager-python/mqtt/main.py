import os
import time

import paho.mqtt.client as paho_mqtt

ROOT_MQTT_BROKER_URL = os.environ.get("ROOT_MQTT_BROKER_URL")
ROOT_MQTT_BROKER_PORT = os.environ.get("ROOT_MQTT_BROKER_PORT")

mqtt_client = None


def reconnect(client):

    FIRST_RECONNECT_DELAY = 1
    RECONNECT_RATE = 2
    MAX_RECONNECT_COUNT = 12
    MAX_RECONNECT_DELAY = 60
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        print("ROOT MQTT: Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            print("ROOT MQTT: Reconnected successfully!")
            return
        except Exception as err:
            print("ROOT MQTT: %s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    print("ROOT MQTT: Reconnect failed after %s attempts. Exiting...", reconnect_count)


def init_mqtt() -> paho_mqtt.Client:
    global mqtt_client
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("ROOT MQTT: Unexpected MQTT disconnection. Attempting to reconnect.")
            reconnect(client)

    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.connect(ROOT_MQTT_BROKER_URL, int(ROOT_MQTT_BROKER_PORT))
    return mqtt_client


def get_mqtt_client():
    if mqtt_client is None:
        return init_mqtt()
    else:
        return mqtt_client
