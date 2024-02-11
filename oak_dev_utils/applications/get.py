import json
from typing import List

import requests

from oak_dev_utils.util.api import create_api_query


def get_applications() -> List:
    url, headers, _ = create_api_query("/api/applications/")
    get_applications_response = requests.get(url, headers=headers)
    get_applications_response_parsed = json.loads(get_applications_response.json())
    return get_applications_response_parsed
