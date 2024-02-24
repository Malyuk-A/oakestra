from http import HTTPStatus
from typing import Any, NamedTuple, Optional, Tuple

import requests
from api.common import SYSTEM_MANAGER_URL
from api.main import flask_app_logger

from oakestra_fl.root_layer.root_fl_manager.api.login import get_login_token


class ApiQuery(NamedTuple):
    url: str
    headers: dict
    data: dict = None


def create_api_query(
    base_url: str, api_endpoint: str, custom_headers: dict = None, data: dict = None
) -> ApiQuery:
    url = f"{base_url}{api_endpoint}"
    headers = custom_headers or {"Authorization": f"Bearer {get_login_token()}"}
    if data and not custom_headers:
        headers["Content-Type"] = "application/json"
    return ApiQuery(url, headers, data)


def create_system_manager_api_query(
    api_endpoint: str, custom_headers: dict = None, data: dict = None
) -> ApiQuery:
    return create_api_query(SYSTEM_MANAGER_URL, api_endpoint, custom_headers, data)


def send_request(
    base_url: str, api_endpoint: str = None, error_msg_subject: str = None
) -> Tuple[HTTPStatus, Optional[Any]]:
    url = base_url
    if api_endpoint is not None:
        url = f"{base_url}{api_endpoint}"

    try:
        response = requests.get(url, verify=False)
        response_status = HTTPStatus(response.status_code)
        if response_status == HTTPStatus.OK:
            return response_status, response.json()
        else:
            return (
                response_status,
                f"{error_msg_subject} request failed with '{response_status}' for '{url}",
            )
    except requests.exceptions.RequestException as e:
        return (
            HTTPStatus.INTERNAL_SERVER_ERROR,
            f"{error_msg_subject} request failed with '{e}' for '{url}",
        )


def send_github_request(api_endpoint: str = None) -> Tuple[HTTPStatus, Optional[Any]]:
    return send_request("https://api.github.com", api_endpoint, "Github")


def check_api_response(
    response: requests.models.Response,
    what_should_happen: str,
    special_msg_on_fail: str = None,
    hide_msg_on_success: bool = False,
) -> None:
    if response.status_code == HTTPStatus:
        if not hide_msg_on_success:
            flask_app_logger.info(f"Success: '{what_should_happen}'")
    else:
        flask_app_logger.error(f"FAILED: '{special_msg_on_fail or what_should_happen}'!")
        flask_app_logger.error("response:", response)


def check_api_response_quietly(
    response: requests.models.Response,
    what_should_happen: str,
    special_msg_on_fail: str = None,
) -> None:
    check_api_response(response, what_should_happen, special_msg_on_fail, hide_msg_on_success=True)
