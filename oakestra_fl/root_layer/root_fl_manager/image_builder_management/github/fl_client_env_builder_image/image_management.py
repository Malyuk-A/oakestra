import os
import shlex
import subprocess

from build_context import get_build_context
from notification_management import notify_about_failed_build_and_terminate
from utils.logging import logger


def prepare_new_image_name_with_tag() -> None:
    full_registry_url = get_build_context().image_registry_url
    cloned_repo = get_build_context().cloned_repo

    image_registry_url = full_registry_url.removeprefix("http://").removeprefix("https://")
    latest_commit_hash = cloned_repo.head.commit.hexsha

    repo_url = cloned_repo.remotes.origin.url
    user_repo_name = repo_url.split("github.com/")[1].split(".git")[0]
    # Note: (docker) image registry URLs do now allow uppercases.
    username = user_repo_name.split("/")[0].lower()
    repo_name = user_repo_name.split("/")[1]

    new_image_name_with_tag = f"{image_registry_url}/{username}/{repo_name}:{latest_commit_hash}"
    logger.debug(f"New image name prepared: '{new_image_name_with_tag}'")

    get_build_context().set_new_image_name_with_tag(new_image_name_with_tag)


def build_repo_specific_fl_client_env_image() -> None:
    # Important: Be very careful how and where you run buildah.
    # If you run buildah incorrectly it can easily kill your host system.
    # (Due to its necessary elevated privileges for building.)
    # E.g. Mismatch between current directory and target Dockerfile to build.
    image_name_with_tag = get_build_context().new_image_name_with_tag
    os.chdir("fl_client_env_image")
    logger.info(f"Start building image: '{image_name_with_tag}'")
    try:
        result = subprocess.run(
            shlex.split(f"buildah build --isolation=chroot -t {image_name_with_tag}"),
            check=False,
            text=True,
        )
        if result.returncode != 0:
            notify_about_failed_build_and_terminate(
                f"Image build for '{image_name_with_tag}' completed with rc != 0; '{result.stderr}'"
            )
    except Exception as e:
        notify_about_failed_build_and_terminate(
            f"Image build process for '{image_name_with_tag}' failed; '{e}'"
        )
    logger.info(f"Finished building image: '{image_name_with_tag}'")


def push_image() -> None:
    image_name_with_tag = get_build_context().new_image_name_with_tag
    logger.info(f"Start pushing image '{image_name_with_tag}'")
    try:
        subprocess.check_call(
            shlex.split(f"buildah push --tls-verify=false  {image_name_with_tag}")
        )
    except Exception as e:
        notify_about_failed_build_and_terminate(
            f"Failed to push '{image_name_with_tag}' to image registry; '{e}'"
        )
    logger.info(f"Finished pushing image '{image_name_with_tag}")
