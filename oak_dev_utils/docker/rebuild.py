import json
import pathlib
import shlex
import subprocess

from oak_dev_utils.docker.enums import OakestraDockerComposeService, RootOrchestratorService
from oak_dev_utils.util.dev_logger import dev_logger

ROOT_ORCHESTRATOR_DOCKER_COMPOSE_FILE_PATH = pathlib.Path(
    "/home/alex/oakestra/root_orchestrator/docker-compose.yml"
)
CLUSTER_ORCHESTRATOR_DOCKER_COMPOSE_FILE_PATH = pathlib.Path(
    "/home/alex/oakestra/cluster_orchestrator/docker-compose.yml"
)


def check_rebuilded_docker_service_status(docker_service: OakestraDockerComposeService):
    inspect_cmd = 'docker inspect -f "{{ json .State }}" ' + str(docker_service)
    result = subprocess.run(
        shlex.split(inspect_cmd),
        check=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    result_output = json.loads(result.stdout)
    service_status = result_output['Status']
    if service_status == "running":
        dev_logger.info(f"'{docker_service}' successfully rebuild - status: '{service_status}'")
    else:
        dev_logger.error(f"'{docker_service}' failed to rebuild - status: '{service_status}'")


def rebuild_docker_service(docker_service: OakestraDockerComposeService):
    rebuild_flags = "-d --build --no-deps --force-recreate"
    if isinstance(docker_service, RootOrchestratorService):
        compose_path = ROOT_ORCHESTRATOR_DOCKER_COMPOSE_FILE_PATH
    else:
        compose_path = CLUSTER_ORCHESTRATOR_DOCKER_COMPOSE_FILE_PATH

    final_cmd = f"docker compose -f {compose_path} up {rebuild_flags} {docker_service}"

    subprocess.run(
        shlex.split(final_cmd),
        check=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    check_rebuilded_docker_service_status(docker_service)
