import api.utils
import requests
from api.main import flask_app_logger

login_token = ""


def login_and_set_token() -> str:
    data = {"username": "Admin", "password": "Admin"}
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    url, headers, data = api.utils.create_system_manager_api_query("/api/auth/login", headers, data)
    try:
        response = requests.post(url, headers=headers, json=data)
    except Exception as e:
        flask_app_logger.error(e)
        exit(1)

    api.utils.check_api_response_quietly(response, what_should_happen="Login")

    global login_token
    login_token = response.json()["token"]
    return login_token


def get_login_token() -> str:
    if login_token == "":
        return login_and_set_token()
    return login_token
