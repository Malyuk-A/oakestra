import argparse

from build_context import BuildContext


def parse_args() -> None:
    parser = argparse.ArgumentParser(description="Process GitHub repository and service ID.")

    parser.add_argument("repo_url", type=str, help="The URL of the GitHub repository.")
    parser.add_argument(
        "image_registry_url",
        type=str,
        help="The URL of the image registry the build image should be pushed to.",
    )
    parser.add_argument("service_id", type=str)
    parser.add_argument(
        "mqtt_url",
        type=str,
        help="The MQTT URL to be able to notify the FL manager about the image build.",
    )
    parser.add_argument("mqtt_port", type=str)
    parser.add_argument("builder_app_name", type=str)

    args = parser.parse_args()

    BuildContext(
        args.repo_url,
        args.image_registry_url,
        args.service_id,
        args.mqtt_url,
        args.mqtt_port,
        args.builder_app_name,
    )
