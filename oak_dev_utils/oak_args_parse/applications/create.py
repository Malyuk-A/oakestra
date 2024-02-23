import argparse
from typing import Any

from oak_dev_utils.applications.create import create_app_via_sla
from oak_dev_utils.login import login_and_set_token
from oak_dev_utils.oak_args_parse.types import Subparsers
from oak_dev_utils.util.SLAs.enum import KnownSLA


def aux_create_application(args: Any) -> None:
    if args.sla:
        create_app_via_sla(args.sla)
    else:
        # More fine grained dynamic app creation could be implemented.
        pass


def prepare_applications_create_argparser(applications_subparsers: Subparsers) -> None:
    HELP_TEXT = "creates a new application"
    applications_create_parser = applications_subparsers.add_parser(
        "create",
        aliases=["c"],
        help=HELP_TEXT,
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    applications_create_parser.add_argument(
        "sla",
        help="creates an application based on a KnowsSLA (if is has its own enum)",
        type=KnownSLA,
        choices=KnownSLA,
        default=KnownSLA.DEFAULT,
    )
    applications_create_parser.set_defaults(func=aux_create_application)
