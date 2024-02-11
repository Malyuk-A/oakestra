import json
from typing import List

import requests

from oak_dev_utils.common import CORE_URL
from oak_dev_utils.dev_logger import dev_logger


def get_applications(bearer_auth_token: str) -> List:

    get_applications_query = {
        "url": f"{CORE_URL}/api/applications/",
        "headers": {
            "Authorization": f"Bearer {bearer_auth_token}",
        },
    }

    get_applications_response = requests.get(
        get_applications_query["url"],
        headers=get_applications_query["headers"],
    )
    get_applications_response_parsed = json.loads(get_applications_response.json())
    return get_applications_response_parsed


def display_applications(applications: List) -> None:
    def log_aux(key: str, value: str) -> None:
        dev_logger.info(f"   {key}: '{value}'")

    dev_logger.info(f"current apps: '{len(applications)}'")
    for i, application in enumerate(applications):
        dev_logger.info(f" App '{i}':")
        log_aux("name", application["application_name"])
        log_aux("ns", application["application_namespace"])
        log_aux("desc", application["application_desc"])
        log_aux("microservices", len(application["microservices"]))


def display_current_applications(bearer_auth_token: str) -> None:
    display_applications(get_applications(bearer_auth_token))
