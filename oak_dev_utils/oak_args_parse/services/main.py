import argparse
from typing import Any

from oak_dev_utils.oak_args_parse.services.deployment import prepare_services_deployment_argparser
from oak_dev_utils.oak_args_parse.services.status import prepare_services_display_argparser
from oak_dev_utils.oak_args_parse.types import Subparsers


def prepare_services_argparsers(subparsers: Subparsers) -> None:
    services_parser = subparsers.add_parser(
        "services",
        aliases=["s"],
        help="command for service(s) related activities",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    def services_parser_print_help(_: Any) -> None:
        services_parser.print_help()

    services_parser.set_defaults(func=services_parser_print_help)

    services_subparsers = services_parser.add_subparsers(
        dest="services commands",
    )

    prepare_services_display_argparser(services_subparsers)
    prepare_services_deployment_argparser(services_subparsers)
