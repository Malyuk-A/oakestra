import argparse
from typing import Tuple

from image_management import (
    build_repo_specific_fl_client_env_image,
    prepare_new_image_name_with_tag,
    push_image,
)
from repo_management import check_cloned_repo, clone_repo
from util_logging import logger


def parse_args() -> Tuple[str, str, str]:
    parser = argparse.ArgumentParser(description="Process GitHub repository and service ID.")
    parser.add_argument("repo_url", type=str, help="The URL of the GitHub repository.")
    parser.add_argument(
        "image_registry_url",
        type=str,
        help="The URL of the image registry the build image should be pushed to.",
    )
    parser.add_argument("service_id", type=str, help="The service ID.")
    args = parser.parse_args()

    repo_url = args.repo_url
    image_registry_url = args.image_registry_url
    service_id = args.service_id
    logger.debug(f"Repo URL: {repo_url}")
    logger.debug(f"Image Registry URL: {image_registry_url}")
    logger.debug(f"Service ID: {service_id}")

    return repo_url, image_registry_url, service_id


def main() -> None:
    repo_url, image_registry_url, service_id = parse_args()
    cloned_repo = clone_repo(repo_url)
    check_cloned_repo(cloned_repo)
    image_name_with_tag = prepare_new_image_name_with_tag(cloned_repo, image_registry_url)
    build_repo_specific_fl_client_env_image(image_name_with_tag)
    push_image(image_name_with_tag)


if __name__ == "__main__":
    main()
