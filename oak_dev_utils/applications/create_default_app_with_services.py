import json

import requests

from oak_dev_utils.util.common import CORE_URL, DEV_UTILS_PATH


def create_default_app_with_services(bearer_auth_token: str) -> None:

    default_SLA = ""
    with open(DEV_UTILS_PATH / "default_SLA.json", "r") as f:
        default_SLA = json.load(f)

    application_creation_query = {
        "url": f"{CORE_URL}/api/application/",
        "headers": {
            "Authorization": f"Bearer {bearer_auth_token}",
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
        print("Successfully created new default application with services")
    else:
        print("FAILED to created new default application with services !!!")
        print("response:", application_creation_response)
