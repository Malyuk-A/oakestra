import argparse
from typing import NamedTuple

from util.logging import logger


class ParsedArgs(NamedTuple):
    repo_url: str
    image_registry_url: str
    service_id: str
    mqtt_url: str
    mqtt_port: str


def parse_args() -> ParsedArgs:
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

    args = parser.parse_args()

    repo_url = args.repo_url
    image_registry_url = args.image_registry_url
    service_id = args.service_id
    mqtt_url = args.mqtt_url
    mqtt_port = args.mqtt_port

    logger.debug(f"Repo URL: {repo_url}")
    logger.debug(f"Image Registry URL: {image_registry_url}")
    logger.debug(f"Service ID: {service_id}")
    logger.debug(f"MQTT URL: {mqtt_url}")
    logger.debug(f"MQTT PORT: {mqtt_port}")

    return ParsedArgs(repo_url, image_registry_url, service_id, mqtt_url, mqtt_port)
