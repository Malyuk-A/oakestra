import json
from typing import List

import requests

from oak_dev_utils.util.api import check_api_response_quietly, create_api_query


def get_applications() -> List:
    url, headers, _ = create_api_query("/api/applications/")
    response = requests.get(url, headers=headers)
    check_api_response_quietly(response, what_should_happen="Get applications")

    get_applications_response_parsed = json.loads(response.json())
    return get_applications_response_parsed
