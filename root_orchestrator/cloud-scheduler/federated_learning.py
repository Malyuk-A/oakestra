from typing import Dict

import requests
from common import SYSTEM_MANAGER_ADDR
from cs_logging import configure_logging

logger = configure_logging()


def handle_fl_job_request_preperations(job: Dict) -> None:
    if len(job.get("instance_list")) == 0:
        return
    API_ENDPOINT = f"/api/fl/{job['applicationID']}/instance"
    try:
        requests.post(SYSTEM_MANAGER_ADDR + API_ENDPOINT)
    except requests.exceptions.RequestException:
        logger.error(f"Calling System Manager '{API_ENDPOINT}' not successful.")
