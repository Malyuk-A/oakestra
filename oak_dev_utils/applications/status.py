from typing import List

from oak_dev_utils.applications.general import get_applications
from oak_dev_utils.login import get_login_token
from oak_dev_utils.util.dev_logger import dev_logger


def display_applications(applications: List) -> None:

    def log_aux(key: str, value: str) -> None:
        dev_logger.info(f"   {key}: '{value}'")

    dev_logger.info(f"Current apps: '{len(applications)}'")
    for i, application in enumerate(applications):
        dev_logger.info(f" App '{i}':")
        log_aux("id", application["applicationID"])
        log_aux("name", application["application_name"])
        log_aux("ns", application["application_namespace"])
        log_aux("desc", application["application_desc"])
        log_aux("microservices", len(application["microservices"]))


def display_current_applications() -> None:
    display_applications(get_applications(get_login_token()))
