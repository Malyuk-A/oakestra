import json
import sys

import paho.mqtt.client as paho_mqtt
from build_context import get_build_context


def _notify_root_fl_manager(topic: str, error_msg: str = None) -> None:
    build_context = get_build_context()
    mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    # mqtt_client.connect(mqtt_url, int(mqtt_port))
    mqtt_client.connect("192.168.178.44", int(build_context.mqtt_port))
    mqtt_client.publish(
        topic=topic,
        payload=json.dumps(
            {
                "service_id": build_context.service_id,
                "image_name_with_tag": build_context.new_image_name_with_tag,
                "builder_app_name": build_context.builder_app_name,
                **({"error_msg": error_msg} if error_msg is not None else {}),
            }
        ),
        qos=1,
        retain=False,
    )


def notify_about_successful_build() -> None:
    _notify_root_fl_manager(topic="image_builder/success")


def notify_about_failed_build_and_terminate(error_msg: str) -> None:
    _notify_root_fl_manager("image_builder/failed", error_msg)
    sys.exit(1)
