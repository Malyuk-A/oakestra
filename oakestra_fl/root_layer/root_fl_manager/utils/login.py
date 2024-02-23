import requests
import utils.api as util_api

login_token = ""


def login_and_set_token() -> str:
    from utils.logging import logger

    logger.debug("R1#" * 10)

    # data = {"username": "Admin", "password": "Admin"}
    data = {"username": "kevin", "password": "kevin"}
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    url, headers, data = util_api.create_system_manager_api_query("/api/auth/login", headers, data)
    logger.debug("R2#" * 10)
    logger.debug("url")
    logger.debug(url)
    logger.debug("haeders")
    logger.debug(headers)
    logger.debug("data")
    logger.debug(data)
    try:
        response = requests.post(url, headers=headers, json=data)
    except Exception as e:
        logger.error(e)
        exit(1)

    logger.debug("R3#" * 10)
    util_api.check_api_response_quietly(response, what_should_happen="Login")
    logger.debug("R4#" * 10)

    global login_token
    login_token = response.json()["token"]
    logger.debug("R5#" * 10)
    return login_token


def get_login_token() -> str:
    if login_token == "":
        return login_and_set_token()
    return login_token
