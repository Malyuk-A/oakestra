import argparse
from typing import Tuple

from utils.logging import logger


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="Process GitHub repository and service ID.")
    parser.add_argument("repo_url", type=str, help="The URL of the GitHub repository.")
    parser.add_argument("service_id", type=str, help="The service ID.")
    args = parser.parse_args()
    repo_url = args.repo_url
    service_id = args.service_id
    logger.debug(f"Repo URL: {repo_url}")
    logger.debug(f"Service ID: {service_id}")
    return repo_url, service_id


def main():
    repo_url, service_id = parse_args()


if __name__ == "__main__":
    main()
