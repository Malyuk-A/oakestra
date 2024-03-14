from http import HTTPStatus

import api.utils
from image_builder_management.repo_management import get_repo_details
from image_builder_management.sla_generator import generate_builder_sla
from utils.logging import logger


class BuilderAppCreationException(Exception):
    pass


class BuilderServiceDeploymentException(Exception):
    pass


def delegate_image_build(service_id: str, repo_url: str, repo_name: str) -> None:
    repo_id, latest_short_commit_hash = get_repo_details(repo_name)
    builder_app_sla = generate_builder_sla(repo_url, repo_id, latest_short_commit_hash, service_id)
    builder_app_name = builder_app_sla["applications"][0]["application_name"]
    logger.debug(
        f"Created builder SLA for service '{service_id}' and repo '{repo_url}': {builder_app_sla}"
    )

    # Note: The called endpoint returns all applications of the user not just the newest inserted one.
    status, json_data = api.utils.handle_request(
        base_url=api.common.SYSTEM_MANAGER_URL,
        http_method=api.common.HttpMethod.POST,
        api_endpoint="/api/application",
        data=builder_app_sla,
        what_should_happen=f"Create new builder app for service '{service_id}' repo '{repo_url}'",
        show_msg_on_success=True,
    )
    if status != HTTPStatus.OK:
        raise BuilderAppCreationException()

    new_builder_app = next(
        (app for app in json_data if app["application_name"] == builder_app_name), None
    )
    if new_builder_app is None:
        raise BuilderAppCreationException()
    builder_service_id = new_builder_app["microservices"][0]

    status, json_data = api.utils.handle_request(
        base_url=api.common.SYSTEM_MANAGER_URL,
        http_method=api.common.HttpMethod.POST,
        api_endpoint=f"/api/service/{builder_service_id}/instance",
        what_should_happen=f"Deploy builder service for '{repo_url}', id '{builder_service_id}'",
        show_msg_on_success=True,
    )
    if status != HTTPStatus.OK:
        raise BuilderServiceDeploymentException()
