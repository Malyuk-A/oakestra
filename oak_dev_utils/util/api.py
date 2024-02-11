from typing import NamedTuple

import requests

from oak_dev_utils.login import get_login_token
from oak_dev_utils.util.common import CORE_URL
from oak_dev_utils.util.dev_logger import dev_logger


class ApiQuery(NamedTuple):
    url: str
    headers: dict
    data: dict = None


def create_api_query(api_endpoint: str, data: dict = None) -> ApiQuery:
    url = f"{CORE_URL}{api_endpoint}"
    headers = {"Authorization": f"Bearer {get_login_token()}"}
    if data:
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
