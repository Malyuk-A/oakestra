import pathlib
import shlex
import subprocess

import git
from util.logging import logger

FL_CLIENT_ENV_IMAGE_DOCKERFILE = pathlib.Path("fl_client_env_image/Dockerfile")


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


def build_repo_specific_fl_client_env_image(image_name_with_tag: str) -> None:
    logger.info("Start testing buildah")
    logger.info("A#" * 10)
    subprocess.check_call(shlex.split("buildah --version"))
    logger.info("B#" * 10)
    subprocess.check_call(shlex.split("buildah images"))
    logger.info("C#" * 10)

    logger.info(f"Start building image: '{image_name_with_tag}'")
    try:
        # subprocess.check_call(
        #     shlex.split(
        #         f"buildah build -f {FL_CLIENT_ENV_IMAGE_DOCKERFILE} -t {image_name_with_tag}"
        #     )
        # )
        result = subprocess.run(
            shlex.split(
                f"buildah build -f {FL_CLIENT_ENV_IMAGE_DOCKERFILE} -t {image_name_with_tag}"
            ),
            check=False,
            # stderr=subprocess.PIPE,
            text=True,
        )
        logger.info("RES#" * 10)
        logger.info(result)
        if result.returncode != 0:
            raise Exception(result)

    except Exception as e:
        logger.critical(f"Exception Triggered: '{e}'")
        raise

    logger.info(f"Finished building image: '{image_name_with_tag}'")

    logger.info("D#" * 10)
    subprocess.check_call(shlex.split("buildah images"))

    logger.info("Finished testing buildah")


def push_image(image_name_with_tag: str) -> None:
    logger.info(f"Start pushing image '{image_name_with_tag}'")
    subprocess.check_call(shlex.split(f"buildah push --tls-verify=false  {image_name_with_tag}"))
    logger.info(f"Finished pushing image '{image_name_with_tag}")
