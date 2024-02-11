import requests

from oak_dev_utils.util.api import check_api_response_quietly, create_api_query

login_token = ""


def login_and_set_token() -> str:
    data = {"username": "Admin", "password": "Admin"}
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    url, headers, data = create_api_query("/api/auth/login", headers, data)
    response = requests.post(url, headers=headers, json=data)
    check_api_response_quietly(response, what_should_happen="Login")

    global login_token
    login_token = response.json()["token"]


def get_login_token() -> str:
    return login_token
