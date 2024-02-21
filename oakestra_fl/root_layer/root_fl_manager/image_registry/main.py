from image_registry.auxiliary import (
    EXTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME,
    EXTERNAL_ROOT_FL_IMAGE_REGISTRY_URL,
    check_registry_reachable,
)
from utils.general import docker
from utils.logging import logger


def push_image_to_root_registry():
    if not check_registry_reachable():
        return 500

    logger.debug("A" * 15)
    found_images = docker.images.list(filters={"reference": EXTERNAL_ROOT_FL_IMAGE_REGISTRY_URL})
    logger.info(found_images)
    logger.debug("B" * 15)

    pulled_image_name = "alpine:latest"
    docker.images.pull(pulled_image_name)

    new_image_name = f"{EXTERNAL_ROOT_FL_IMAGE_REGISTRY_NAME}/alpine:latest-testalex4"
    logger.debug("C" * 15)

    docker.images.get(pulled_image_name).tag(new_image_name)

    logger.debug("D" * 15)

    return

    docker.images.push(new_image_name)

    logger.debug("X" * 15)
    found_images = docker.images.list(filters={"reference": EXTERNAL_ROOT_FL_IMAGE_REGISTRY_URL})
    logger.debug("Y" * 15)
    logger.info(found_images)
    logger.info("Z" * 15)
