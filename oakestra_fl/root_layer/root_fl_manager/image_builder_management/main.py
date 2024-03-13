from api.utils import create_system_manager_api_query
from image_builder_management.repo_management import get_repo_details
from image_builder_management.sla_generator import generate_builder_sla
from utils.logging import logger


def delegate_image_build(service_id: str, repo_url: str, repo_name: str) -> None:
    repo_id, latest_short_commit_hash = get_repo_details(repo_name)
    builder_app_sla = generate_builder_sla(repo_url, repo_id, latest_short_commit_hash, service_id)
    logger.debug("AAAAAAA")

    url, headers, _ = create_system_manager_api_query("/api/application", data=builder_app_sla)
    logger.debug("BBBBBBB")

    # response = requests.put(url, json=service)
    # logger.debug(url)
    # logger.debug(headers)
    # logger.debug("G#" * 10)
    # response = requests.get(url, headers=headers)

    # logger.debug("H#" * 10)
    # logger.debug(response)
    # logger.debug(response.json())
    # logger.debug("h-" * 10)

    pass
    # prepare/build SLA for IMAGE BUILDER
    # provide the url and service id as build args/params
    # call RO API
