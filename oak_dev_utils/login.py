import requests

import oak_dev_utils.util.api as oak_api

login_token = ""


def login_and_set_token() -> str:
    data = {"username": "Admin", "password": "Admin"}
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    url, headers, data = oak_api.create_api_query("/api/auth/login", headers, data)
    response = requests.post(url, headers=headers, json=data)
    oak_api.check_api_response_quietly(response, what_should_happen="Login")

    global login_token
    login_token = response.json()["token"]
    return login_token


def get_login_token() -> str:
    if login_token == "":
        return login_and_set_token()
    return login_token
