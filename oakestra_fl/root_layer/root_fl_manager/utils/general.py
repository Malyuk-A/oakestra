import os

# Note: Instead of using python-on-whales the more mature docker SDK python lib
# should not require/install the docker CLI to work.
import docker as docker_sdk

ROOT_FL_IMAGE_REGISTRY_DNS_NAME = "root_fl_image_registry"
ROOT_FL_IMAGE_REGISTRY_PORT = os.environ.get("ROOT_FL_IMAGE_REGISTRY_PORT")

GITHUB_PREFIX = "https://github.com/"

docker = docker_sdk.from_env()
