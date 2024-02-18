import os
from typing import Dict, List

import requests

ROOT_FL_MANAGER_PORT = 5072
ROOT_FL_MANAGER_ADDR = f"http://{os.environ.get('SYSTEM_MANAGER_URL')}:{ROOT_FL_MANAGER_PORT}"


def delegate_fl_service_request(job: Dict) -> None:
    API_ENDPOINT = f"/api/fl/{job['applicationID']}/instance"
    try:
        requests.post(SYSTEM_MANAGER_ADDR + API_ENDPOINT)
    except requests.exceptions.RequestException:
        print(f"Calling System Manager '{API_ENDPOINT}' not successful.")


def check_for_fl_services(microservices: List[Dict]):
    for service in microservices:
        if service.get("virtualization") == "ml_repo" and service.get("code"):
            delegate_fl_service_request(service)
