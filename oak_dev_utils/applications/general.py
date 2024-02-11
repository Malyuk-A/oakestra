import json
from typing import List

import requests

from oak_dev_utils.login import get_login_token
from oak_dev_utils.util.common import CORE_URL, DEV_UTILS_PATH
from oak_dev_utils.util.dev_logger import dev_logger


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


def create_default_app_with_services() -> None:

    default_SLA = ""
    with open(DEV_UTILS_PATH / "applications" / "default_SLA.json", "r") as f:
        default_SLA = json.load(f)

    application_creation_query = {
        "url": f"{CORE_URL}/api/application/",
        "headers": {
            "Authorization": f"Bearer {get_login_token()}",
            "Content-Type": "application/json",
        },
        "data": default_SLA,
    }

    application_creation_response = requests.post(
        application_creation_query["url"],
        headers=application_creation_query["headers"],
        json=application_creation_query["data"],
    )

    if application_creation_response.status_code == 200:
        dev_logger.info("Successfully created new default application with services")
    else:
        dev_logger.error("FAILED to created new default application with services !!!")
        dev_logger.error("response:", application_creation_response)


def delete_application(app_id: str) -> None:
    application_deletion_query = {
        "url": f"{CORE_URL}/api/application/{app_id}",
        "headers": {
            "Authorization": f"Bearer {get_login_token()}",
        },
    }

    application_deletion_response = requests.delete(
        application_deletion_query["url"],
        headers=application_deletion_query["headers"],
    )

    if application_deletion_response.status_code == 200:
        dev_logger.info(f"Successfully deleted application '{app_id}'")
    else:
        dev_logger.error("FAILED to delete application '{app_id}'!")
        dev_logger.error("response:", application_deletion_response)


# def delete_all_applications(bearer_auth_token: str) -> None:
