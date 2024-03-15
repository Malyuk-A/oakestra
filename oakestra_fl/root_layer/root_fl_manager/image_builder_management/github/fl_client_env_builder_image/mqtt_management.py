import json
import shlex
import subprocess
import sys

from utils.logging import logger


def notify_root_fl_manager(
    mqtt_url: str,
    mqtt_port: str,
    service_id: str,
    image_name_with_tag: str,
    builder_app_name: str,
) -> None:
    message = (
        json.dumps(
            {
                "service_id": service_id,
                "image_name_with_tag": image_name_with_tag,
                "builder_app_name": builder_app_name,
            }
        ),
    )
    mqtt_cmd = " ".join(
        (
            "mosquitto_pub",
            "-h",
            # mqtt_url,
            "192.168.178.44",
            "-p",
            mqtt_port,
            "-t",
            "image_builder/success",
            "-q",
            "1",
            "-m",
            str(message),
        )
    )

    try:
        result = subprocess.run(
            shlex.split(mqtt_cmd),
            check=False,
            # stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            raise Exception(result)

    except Exception as e:
        logger.critical(f"Exception Triggered: '{e}'")
        sys.exit(1)

    # Note: The client paho_mqtt.Client works fine when executed directly from within the container.
    # I.e. after attaching to it e.g. via ctr.
    # However, when this client is run as part of a command chain from the provided CMD the mqtt_client cannot connect.
    # The error is thrown deep in the python socket implementation.
    # An easy workaround is to use the apt package for the mosquitto client instead.

    # mqtt_client = paho_mqtt.Client(paho_mqtt.CallbackAPIVersion.VERSION1)
    # mqtt_client.connect(mqtt_url, int(mqtt_port))
    # mqtt_client.publish(
    #     topic="image_builder/success",
    #     payload=json.dumps(
    #         {
    #             "service_id": service_id,
    #             "image_name_with_tag": image_name_with_tag,
    #             "builder_app_name": builder_app_name,
    #         }
    #     ),
    #     qos=1,
    #     retain=False,
    # )
