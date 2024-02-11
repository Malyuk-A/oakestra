import json

import requests

from oak_dev_utils.util.api import check_api_response, create_api_query
from oak_dev_utils.util.common import DEV_UTILS_PATH
from oak_dev_utils.util.SLAs import enum


def create_app_via_sla(knwon_sla: enum) -> None:
    sla_file_name = f"{knwon_sla}.SLA.json"
    SLA = ""
    with open(DEV_UTILS_PATH / "util" / "SLAs" / sla_file_name, "r") as f:
        SLA = json.load(f)

    url, headers, data = create_api_query("/api/application/", data=SLA)
    response = requests.post(url, headers=headers, json=data)
    check_api_response(response, what_should_happen=f"Create '{sla_file_name}'")
