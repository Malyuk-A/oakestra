import pathlib
import shlex

FL_CLIENT_ENV_IMAGE_DOCKERFILE = pathlib.Path("fl_client_env_image/Dockerfile")
import subprocess

from utils.logging import logger

# import docker as docker_sdk

# docker = docker_sdk.from_env()


def build_repo_specific_fl_client_env_image():
    print("A" * 10)

    # res = subprocess.run(
    #     shlex.split("buildah --version"),
    #     check=False,
    #     stderr=subprocess.PIPE,
    #     # stdout=subprocess.PIPE,
    #     text=True,
    # )
    # print(res)
    # res = subprocess.run(
    #     shlex.split("buildah pull alpine"),
    #     check=False,
    #     stderr=subprocess.PIPE,
    #     # stdout=subprocess.PIPE,
    #     text=True,
    # )
    # print(res)
    # res = subprocess.run(
    #     shlex.split("buildah images"),
    #     check=False,
    #     stderr=subprocess.PIPE,
    #     # stdout=subprocess.PIPE,
    #     text=True,
    # )
    # print(res)

    res = subprocess.run(
        shlex.split(f"buildah build -f {FL_CLIENT_ENV_IMAGE_DOCKERFILE} -t bts:latest"),
        check=False,
        stderr=subprocess.PIPE,
        # stdout=subprocess.PIPE,
        text=True,
    )
    print(res)

    res = subprocess.run(
        shlex.split("buildah images"),
        check=False,
        stderr=subprocess.PIPE,
        # stdout=subprocess.PIPE,
        text=True,
    )
    print(res)

    # docker.images.build(path=FL_CLIENT_ENV_IMAGE_DOCKERFILE, tag="testinga")
    # print("B" * 10)
    # images = docker.images.list()
    # print("C" * 10)
    # print(images)
    # for image in images:
    #     print(f"Image ID: {image.id}, Tags: {image.tags}")
