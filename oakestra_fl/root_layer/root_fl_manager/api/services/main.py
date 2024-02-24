from typing import Dict

import requests
from api.main import flask_app_logger
from api.utils import create_system_manager_api_query


def update_service_image(service: Dict, existing_image_name: str) -> None:
    service["image"] = existing_image_name
    service_id = service["microserviceID"]
    flask_app_logger.debug("E#" * 10)

    url, headers, _ = create_system_manager_api_query(f"/api/services/{service_id}")
    flask_app_logger.debug("F#" * 10)

    # response = requests.put(url, json=service)
    flask_app_logger.debug(url)
    flask_app_logger.debug(headers)
    flask_app_logger.debug("G#" * 10)
    response = requests.get(url, headers=headers)

    flask_app_logger.debug("H#" * 10)
    flask_app_logger.debug(response)
    flask_app_logger.debug(response.json())
    flask_app_logger.debug("h-" * 10)
