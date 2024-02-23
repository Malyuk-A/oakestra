import argparse
from typing import Any

from oak_dev_utils.login import login_and_set_token
from oak_dev_utils.oak_args_parse.types import Subparsers
from oak_dev_utils.services.deployment import (
    deploy_new_instance,
    undeploy_all_instances_of_service,
    undeploy_instance,
)


def aux_deploy_instances(args: Any):
    if args.instancenumber:
        if args.instancenumber == "all":
            undeploy_all_instances_of_service(args.service_id)
            pass
        else:
            undeploy_instance(args.service_id, args.instancenumber)
    else:
        deploy_new_instance(args.service_id)


def prepare_services_deployment_argparser(services_subparsers: Subparsers) -> None:
    HELP_TEXT = "deploys or undeploys an instance of a service"
    services_deployment_parser = services_subparsers.add_parser(
        "deployment",
        aliases=["d"],
        help=HELP_TEXT,
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    services_deployment_parser.add_argument(
        "service_id",
        type=str,
    )
    services_deployment_parser.add_argument(
        "--instancenumber",
        "-u",
        type=str,
    )
    services_deployment_parser.set_defaults(func=aux_deploy_instances)
