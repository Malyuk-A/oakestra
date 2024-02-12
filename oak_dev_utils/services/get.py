import json
from typing import List

import requests

from oak_dev_utils.util.api import check_api_response_quietly, create_api_query


def get_all_services(app_id: str = None) -> List:
    url, headers, _ = create_api_query(f"/api/services/{app_id or ''}")
    response = requests.get(url, headers=headers)
    check_api_response_quietly(
        response,
        what_should_happen=(
            f"Get all services of app '{app_id}" if app_id is not None else "Get all services"
        ),
    )
    get_all_services_response_parsed = json.loads(response.json())
    return get_all_services_response_parsed


def get_single_service(service_id: str):
    url, headers, _ = create_api_query(f"/api/service/{service_id}")
    response = requests.get(url, headers=headers)
    check_api_response_quietly(
        response,
        what_should_happen=(f"Get single service '{service_id}'"),
    )
    get_single_service_response_parsed = json.loads(response.json())
    return get_single_service_response_parsed
