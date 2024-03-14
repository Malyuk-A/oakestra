from http import HTTPStatus

import api.utils
from image_builder_management.repo_management import get_repo_details
from image_builder_management.sla_generator import generate_builder_sla
from utils.logging import logger


class BuilderAppCreationException(Exception):
    pass


def delegate_image_build(service_id: str, repo_url: str, repo_name: str) -> None:
    repo_id, latest_short_commit_hash = get_repo_details(repo_name)
    builder_app_sla = generate_builder_sla(repo_url, repo_id, latest_short_commit_hash, service_id)
    logger.debug("AAAAAAA")
    logger.debug(builder_app_sla)
    logger.debug("aaaaaaaa")

    status, json_data = api.utils.handle_request(
        base_url=api.common.SYSTEM_MANAGER_URL,
        http_method=api.common.HttpMethod.POST,
        api_endpoint="/api/application",
        data=builder_app_sla,
        what_should_happen="Create new builder application",
    )
    if status != HTTPStatus.OK:
        raise BuilderAppCreationException()

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
