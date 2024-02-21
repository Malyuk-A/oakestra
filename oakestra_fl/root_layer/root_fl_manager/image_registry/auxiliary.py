import requests
from utils.general import (
    ROOT_FL_IMAGE_REGISTRY_DNS_NAME,
    ROOT_FL_IMAGE_REGISTRY_EXTERNAL_PORT,
    ROOT_FL_IMAGE_REGISTRY_INTERNAL_PORT,
    get_ip_address_from_dns_name,
)
from utils.logging import logger

# Note: We need external and internal names & urls to handle different usecases.
# E.g. internal:
# When checking if the colocated registry is online we use an HTTP request
# using the registry's DNS docker service name and internal port (5000).
# external:
# When using the host's docker daemon (via the docker socket volume)
# we are working directly on the host machine. The host is not part of this dockerized DNS network.
# Thus we need to specify the container IP and the externally facing port (5073).

INTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME = (
    f"{ROOT_FL_IMAGE_REGISTRY_DNS_NAME}:{ROOT_FL_IMAGE_REGISTRY_INTERNAL_PORT}"
)

EXTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME = (
    f"{get_ip_address_from_dns_name()}:{ROOT_FL_IMAGE_REGISTRY_EXTERNAL_PORT}"
)

INTERNAL_ROOT_FL_IMAGE_REGISTRY_URL = f"http://{INTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME}"
EXTERNAL_ROOT_FL_IMAGE_REGISTRY_URL = f"http://{EXTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME}"


def check_registry_reachable() -> bool:
    try:
        response = requests.get(INTERNAL_ROOT_FL_IMAGE_REGISTRY_URL)
        if response.status_code == 200:
            return True
        else:
            logger.error(
                f"Root Image Registry is not reachable. Status code: {response.status_code}"
            )
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Error reaching the registry: {e}")
        return False
