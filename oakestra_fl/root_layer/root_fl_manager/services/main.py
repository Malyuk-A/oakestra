from typing import Dict

import requests
from utils.general import SYSTEM_MANAGER_URL
from utils.logging import logger


def update_service_image(service: Dict, existing_image_name: str) -> None:
    service["image"] = existing_image_name
    service_id = service["microserviceID"]
    url = f"{SYSTEM_MANAGER_URL}/api/services/{service_id}"
    logger.debug("E#" * 10)
    logger.debug(url)
    logger.debug("e-" * 10)
    response = requests.put(url, json=service)
    logger.debug("F#" * 10)
    logger.debug(response)
    logger.debug(response.json())
    logger.debug("f-" * 10)
