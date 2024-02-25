import json

import paho.mqtt.client as paho_mqtt


def notify_root_fl_manager(
    mqtt_url: str,
    mqtt_port: str,
    service_id: str,
    image_name_with_tag: str,
) -> None:
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.connect(mqtt_url, int(mqtt_port))
    mqtt_client.publish(
        topic="image_builder/success",
        payload=json.dumps({"service_id": service_id, "image_name_with_tag": image_name_with_tag}),
        qos=1,
        retain=False,
    )
