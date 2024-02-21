from image_registry.auxiliary import (
    FULL_ROOT_FL_IMAGE_REGISTRY_NAME,
    check_registry_reachable,
    get_current_registry_images,
)
from utils.general import docker
from utils.logging import logger


def push_image_to_root_registry():
    if not check_registry_reachable():
        return 500

    logger.debug("A" * 15)
    logger.info(get_current_registry_images())
    logger.debug("a" * 15)

    pulled_image_name = "alpine:latest"
    docker.images.pull(pulled_image_name)

    # new_image_name = f"{EXTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME}/alpinum:latest-testalex6"
    # new_image_name = "192.168.178.44:5073/alpinum:latest-testalex7"
    new_image_name = f"{FULL_ROOT_FL_IMAGE_REGISTRY_NAME}/alpinum3:latest"
    logger.debug("B" * 15)

    docker.images.get(pulled_image_name).tag(new_image_name)

    docker.images.push(new_image_name)

    logger.debug("Z" * 15)
    logger.info(get_current_registry_images())
    logger.info("z" * 15)
