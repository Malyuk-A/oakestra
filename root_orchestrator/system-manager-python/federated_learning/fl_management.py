import os
from typing import Dict, List

import requests

ROOT_FL_MANAGER_PORT = os.environ.get("ROOT_FL_MANAGER_PORT")
ROOT_FL_MANAGER_URL = os.environ.get("ROOT_FL_MANAGER_URL")
ROOT_FL_MANAGER_ADDR = f"http://{ROOT_FL_MANAGER_URL}:{ROOT_FL_MANAGER_PORT}"


def delegate_fl_service_request(service: Dict) -> None:
    api_endpoint = "/api/fl-services/"
    url = ROOT_FL_MANAGER_ADDR + api_endpoint
    try:
        requests.post(url, json=service)
    except requests.exceptions.RequestException:
        print(f"Calling Root FL Manager '{url}' not successful.")


def check_for_fl_services(microservices: List[Dict]):
    print("RE+" * 10)
    for service in microservices:
        if service.get("virtualization") == "ml-repo" and service.get("code"):
            delegate_fl_service_request(service)
