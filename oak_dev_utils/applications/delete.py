import requests

from oak_dev_utils.applications.get import get_applications
from oak_dev_utils.util.api import check_api_response, create_api_query


def delete_application(app_id: str) -> None:
    url, headers, _ = create_api_query(f"/api/application/{app_id}")
    response = requests.delete(url, headers=headers)
    check_api_response(response, what_should_happen=f"Delete application '{app_id}'")


def delete_all_applications() -> None:
    for app in get_applications():
        delete_application(app["applicationID"])
    
