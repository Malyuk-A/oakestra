import json
from typing import List

import requests

from oak_dev_utils.util.api import create_API_query


def get_applications(bearer_auth_token: str) -> List:

    get_applications_query = create_API_query(
        "/api/applications/",
    )
    get_applications_response = requests.get(
        get_applications_query["url"],
        headers=get_applications_query["headers"],
    )
    get_applications_response_parsed = json.loads(get_applications_response.json())
    return get_applications_response_parsed
