import pathlib

import docker as docker_sdk

docker = docker_sdk.from_env()

# FL_CLIENT_ENV_IMAGE_DOCKERFILE = pathlib.Path("fl_client_env_image/Dockerfile")


def build_repo_specific_fl_client_env_image():
    print("A" * 10)
    exit(1)
    docker.images.build(path=FL_CLIENT_ENV_IMAGE_DOCKERFILE, tag="testinga")
    print("B" * 10)
    images = docker.images.list()
    print("C" * 10)
    print(images)
    for image in images:
        print(f"Image ID: {image.id}, Tags: {image.tags}")
