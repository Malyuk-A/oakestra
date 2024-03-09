import os
import shlex
import subprocess
import sys

import buildah
import git
from util.common import FL_ENV_PATH, run_in_bash
from util.logging import logger


def prepare_new_image_name_with_tag(
    cloned_repo: git.repo.base.Repo, image_registry_url: str
) -> str:
    image_registry_url = image_registry_url.removeprefix("http://").removeprefix("https://")
    latest_commit_hash = cloned_repo.head.commit.hexsha

    repo_url = cloned_repo.remotes.origin.url
    user_repo_name = repo_url.split("github.com/")[1].split(".git")[0]
    # Note: (docker) image registry URLs do now allow uppercases.
    username = user_repo_name.split("/")[0].lower()
    repo_name = user_repo_name.split("/")[1]

    new_image_name_with_tag = f"{image_registry_url}/{username}/{repo_name}:{latest_commit_hash}"
    logger.debug(f"New image name prepared: '{new_image_name_with_tag}'")
    return new_image_name_with_tag


def prepare_and_resolve_dependencies() -> None:
    print("A" * 10)
    run_in_bash("conda activate")
    run_in_bash(f"conda env update --file {FL_ENV_PATH}/conda.yaml ")
    run_in_bash("conda deactivate")
    print("Z" * 10)


def build_repo_specific_fl_client_env_image(image_name_with_tag: str) -> None:

    buildah.

    # Important: Be very careful how and where you run buildah.
    # If you run buildah incorrectly it can easily kill your host system.
    # (Due to its necessary elevated privileges for building.)
    # E.g. Mismatch between current directory and target Dockerfile to build.
    os.chdir("fl_client_env_image")
    logger.info(f"Start building image: '{image_name_with_tag}'")
    try:
        # subprocess.check_call(
        #     shlex.split(
        #         f"buildah build -f {FL_CLIENT_ENV_IMAGE_DOCKERFILE} -t {image_name_with_tag}"
        #     )
        # )
        result = subprocess.run(
            shlex.split(f"buildah build -t {image_name_with_tag}"),
            check=False,
            # stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            raise Exception(result)

    except Exception as e:
        logger.critical(f"Exception Triggered: '{e}'")
        sys.exit(27)
        # raise -> This might be able to kill my docker host farm ............ wtf

    logger.info(f"Finished building image: '{image_name_with_tag}'")


def push_image(image_name_with_tag: str) -> None:
    logger.info(f"Start pushing image '{image_name_with_tag}'")
    subprocess.check_call(shlex.split(f"buildah push --tls-verify=false  {image_name_with_tag}"))
    logger.info(f"Finished pushing image '{image_name_with_tag}")
