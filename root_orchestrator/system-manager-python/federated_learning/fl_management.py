import pathlib
import shlex
import subprocess
from typing import Dict, List

from python_on_whales import DockerClient, docker

ROOT_FL_MANAGER_CONTAINER_NAME = "root_fl_manager"

ROOT_FL_MANAGER_DOCKER_COMPOSE_LINK_PATH = pathlib.Path(
    "federated_learning/fl_root_manager_docker_compose_link.yml"
)


def is_fl_root_mananger_running() -> bool:
    running_containers = docker.ps()
    for container in running_containers:
        print("container name: ", container.name)

        if container.name and container.name == ROOT_FL_MANAGER_CONTAINER_NAME:
            root_fl_manager_container = running_containers[ROOT_FL_MANAGER_CONTAINER_NAME]
            root_fl_manager_container_state = root_fl_manager_container.attrs["State"]
            root_fl_manager_container_status = root_fl_manager_container_state["Status"]
            return root_fl_manager_container_status == "RUNNING"
    return False


def start_fl_root_manager() -> None:
    print("A" * 15)

    docker_client = DockerClient(compose_files=[ROOT_FL_MANAGER_DOCKER_COMPOSE_LINK_PATH])
    print("B" * 15)
    docker_client.compose.up()

    # try:
    #     subprocess.check_call(
    #         shlex.split(f"docker-compose -f {ROOT_FL_MANAGER_DOCKER_COMPOSE_LINK_PATH} up")
    #     )
    # except subprocess.CalledProcessError as e:
    #     print(f"An error occurred while trying to start Docker Compose: {e}")
    # else:
    #     print("Docker Compose started successfully.")

    print("C" * 15)


def check_for_fl_services(microservices: List[Dict]):
    already_checked_fl_root_manager_running = False
    for service in microservices:
        if (
            service.get("virtualization") == "docker"
            and service.get("code")
            and service.get("code").startswith("https://github.com/")
        ):
            if not already_checked_fl_root_manager_running:
                if not is_fl_root_mananger_running():
                    start_fl_root_manager()
                already_checked_fl_root_manager_running = True
