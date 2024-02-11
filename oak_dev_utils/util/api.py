from typing import NamedTuple

import requests

# Hack to resolve circular dependency issues.
import oak_dev_utils.login as oak_dev_login
from oak_dev_utils.util.common import CORE_URL
from oak_dev_utils.util.dev_logger import dev_logger


class ApiQuery(NamedTuple):
    url: str
    headers: dict
    data: dict = None


def create_api_query(api_endpoint: str, custom_headers: dict = None, data: dict = None) -> ApiQuery:
    url = f"{CORE_URL}{api_endpoint}"
    headers = custom_headers or {"Authorization": f"Bearer {oak_dev_login.get_login_token()}"}
    if data and not custom_headers:
        headers["Content-Type"] = "application/json"
    return ApiQuery(url, headers, data)


def check_api_response(
    response: requests.models.Response,
    what_should_happen: str,
    special_msg_on_fail: str = None,
    hide_msg_on_success: bool = False,
) -> None:
    if response.status_code == 200:
        if not hide_msg_on_success:
            dev_logger.info(f"Success: '{what_should_happen}'")
    else:
        dev_logger.error(f"FAILED: '{special_msg_on_fail or what_should_happen}'!")
        dev_logger.error("response:", response)


def check_api_response_quietly(
    response: requests.models.Response,
    what_should_happen: str,
    special_msg_on_fail: str = None,
) -> None:
    check_api_response(response, what_should_happen, special_msg_on_fail, hide_msg_on_success=True)
