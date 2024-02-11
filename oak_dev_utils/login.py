import requests

from oak_dev_utils.util.common import CORE_URL

login_query = {
    "url": f"{CORE_URL}/api/auth/login",
    "headers": {"accept": "application/json", "Content-Type": "application/json"},
    "data": {
        "username": "Admin",
        "password": "Admin",
    },
}


def login_and_get_token() -> str:
    login_response = requests.post(
        login_query["url"], headers=login_query["headers"], json=login_query["data"]
    )
    bearer_auth_token = login_response.json()["token"]
    return bearer_auth_token
