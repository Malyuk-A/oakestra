from oak_dev_utils.login import get_login_token
from oak_dev_utils.util.common import CORE_URL


def create_API_query(api_endpoint: str, data: dict = None) -> dict:
    query = {
        "url": f"{CORE_URL}{api_endpoint}",
        "headers": {
            "Authorization": f"Bearer {get_login_token()}",
        },
    }
    if data:
        query["headers"]["Content-Type"] = "application/json"
        query["data"] = data

    return query
