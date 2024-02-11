import requests

from oak_dev_utils.util.common import CORE_URL

login_token = ""

login_query = {
    "url": f"{CORE_URL}/api/auth/login",
    "headers": {"accept": "application/json", "Content-Type": "application/json"},
    "data": {
        "username": "Admin",
        "password": "Admin",
    },
}


def login_and_set_token() -> str:
    login_response = requests.post(
        login_query["url"], headers=login_query["headers"], json=login_query["data"]
    )
    global login_token
    login_token = login_response.json()["token"]


def get_login_token() -> str:
    return login_token
