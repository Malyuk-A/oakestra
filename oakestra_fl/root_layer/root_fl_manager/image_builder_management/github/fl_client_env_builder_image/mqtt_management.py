import json

import paho.mqtt.client as paho_mqtt


def notify_root_fl_manager(
    mqtt_url: str,
    mqtt_port: str,
    service_id: str,
    image_name_with_tag: str,
    builder_app_name: str,
) -> None:
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    # mqtt_client.connect(mqtt_url, int(mqtt_port))
    mqtt_client.connect("192.168.178.44", int(mqtt_port))
    mqtt_client.publish(
        topic="image_builder/success",
        payload=json.dumps(
            {
                "service_id": service_id,
                "image_name_with_tag": image_name_with_tag,
                "builder_app_name": builder_app_name,
            }
        ),
        qos=1,
        retain=False,
    )
