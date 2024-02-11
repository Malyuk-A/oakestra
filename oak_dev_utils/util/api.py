from typing import NamedTuple

from oak_dev_utils.login import get_login_token
from oak_dev_utils.util.common import CORE_URL


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
