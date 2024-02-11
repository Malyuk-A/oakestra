import json

import requests

from oak_dev_utils.util.api import check_api_response, create_api_query
from oak_dev_utils.util.common import DEV_UTILS_PATH


def create_default_app_with_services() -> None:
    default_SLA = ""
    with open(DEV_UTILS_PATH / "applications" / "default_SLA.json", "r") as f:
        default_SLA = json.load(f)

    url, headers, data = create_api_query("/api/application/", default_SLA)
    response = requests.post(url, headers=headers, json=data)
    check_api_response(response, what_should_happen="Create new default application with services")
