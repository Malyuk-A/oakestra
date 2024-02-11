import json

import requests

from oak_dev_utils.util.api import create_API_query
from oak_dev_utils.util.common import DEV_UTILS_PATH
from oak_dev_utils.util.dev_logger import dev_logger


def create_default_app_with_services() -> None:

    default_SLA = ""
    with open(DEV_UTILS_PATH / "applications" / "default_SLA.json", "r") as f:
        default_SLA = json.load(f)

    application_creation_query = create_API_query("/api/application/", default_SLA)
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
