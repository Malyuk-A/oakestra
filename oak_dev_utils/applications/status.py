from oak_dev_utils.applications.get import get_applications
from oak_dev_utils.util.dev_logger import dev_logger


def display_current_applications() -> None:
    current_applications = get_applications()

    def log_aux(key: str, value: str) -> None:
        dev_logger.info(f"   {key}: '{value}'")

    dev_logger.info(f"Current apps: '{len(current_applications)}'")
    for i, application in enumerate(current_applications):
        dev_logger.info(f" App '{i}':")
        log_aux("id", application["applicationID"])
        log_aux("name", application["application_name"])
        log_aux("ns", application["application_namespace"])
        log_aux("desc", application["application_desc"])
        log_aux(
            "microservices",
            f"{len(application['microservices'])}: {application['microservices']}",
        )
