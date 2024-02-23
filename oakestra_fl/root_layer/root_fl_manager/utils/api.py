from http import HTTPStatus
from typing import NamedTuple

import requests
from utils.general import SYSTEM_MANAGER_URL
from utils.logging import logger
from utils.login import get_login_token


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


def check_api_response(
    response: requests.models.Response,
    what_should_happen: str,
    special_msg_on_fail: str = None,
    hide_msg_on_success: bool = False,
) -> None:
    if response.status_code == HTTPStatus:
        if not hide_msg_on_success:
            logger.info(f"Success: '{what_should_happen}'")
    else:
        logger.error(f"FAILED: '{special_msg_on_fail or what_should_happen}'!")
        logger.error("response:", response)


def check_api_response_quietly(
    response: requests.models.Response,
    what_should_happen: str,
    special_msg_on_fail: str = None,
) -> None:
    check_api_response(response, what_should_happen, special_msg_on_fail, hide_msg_on_success=True)
