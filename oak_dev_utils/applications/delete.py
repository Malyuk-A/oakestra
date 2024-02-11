import requests

from oak_dev_utils.util.api import create_API_query
from oak_dev_utils.util.dev_logger import dev_logger


def delete_application(app_id: str) -> None:
    create_API_query
    application_deletion_query = create_API_query(f"/api/application/{app_id}")
    application_deletion_response = requests.delete(
        application_deletion_query["url"],
        headers=application_deletion_query["headers"],
    )

    if application_deletion_response.status_code == 200:
        dev_logger.info(f"Successfully deleted application '{app_id}'")
    else:
        dev_logger.error("FAILED to delete application '{app_id}'!")
        dev_logger.error("response:", application_deletion_response)


# def delete_all_applications(bearer_auth_token: str) -> None:
