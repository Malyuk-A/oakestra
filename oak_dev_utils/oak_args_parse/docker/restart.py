import argparse
from typing import Any

from oak_dev_utils.docker.enums import ClusterOrchestratorService, RootOrchestratorService
from oak_dev_utils.docker.rebuild import rebuild_docker_service
from oak_dev_utils.docker.restart import restart_docker_service
from oak_dev_utils.oak_args_parse.types import Subparsers


def aux_restart_docker_service(args: Any):
    if args.rebuild:
        rebuild_docker_service(args.service)
    else:
        restart_docker_service(args.service)


def prepare_docker_restart_root_orchestrator_service_parser(
    docker_restart_subparser: Subparsers,
) -> None:
    docker_restart_root_orchestrator_service_parser = docker_restart_subparser.add_parser(
        "root_orchestrator",
        aliases=["ro"],
    )
    docker_restart_root_orchestrator_service_parser.add_argument(
        "service",
        help="testing",
        type=RootOrchestratorService,
        choices=RootOrchestratorService,
    )
    docker_restart_root_orchestrator_service_parser.set_defaults(func=aux_restart_docker_service)


def prepare_docker_restart_cluster_orchestrator_service_parser(
    docker_rebuild_subparser: Subparsers,
) -> None:
    docker_restart_cluster_orchestrator_service_parser = docker_rebuild_subparser.add_parser(
        "cluster_orchestrator",
        aliases=["co"],
    )
    docker_restart_cluster_orchestrator_service_parser.add_argument(
        "service",
        help="testing",
        type=ClusterOrchestratorService,
        choices=ClusterOrchestratorService,
    )
    docker_restart_cluster_orchestrator_service_parser.set_defaults(func=aux_restart_docker_service)


def prepare_docker_restart_argparser(docker_subparsers: Subparsers) -> None:
    HELP_TEXT = "restarts a docker compose service"
    docker_restart_parser = docker_subparsers.add_parser(
        "restarts",
        aliases=["r"],
        help=HELP_TEXT,
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    docker_restart_parser.add_argument(
        "-r",
        "--rebuild",
        help="rebuild the service",
        action="store_true",
    )
    docker_restart_subparsers = docker_restart_parser.add_subparsers()
    prepare_docker_restart_root_orchestrator_service_parser(docker_restart_subparsers)
    prepare_docker_restart_cluster_orchestrator_service_parser(docker_restart_subparsers)
