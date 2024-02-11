import argparse
from typing import Any

from oak_dev_utils.applications.default import create_default_app_with_services
from oak_dev_utils.oak_args_parse.types import Subparsers


def aux_create_application(args: Any) -> None:
    if args.default:
        create_default_app_with_services()
    else:
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
        "-d",
        "--default",
        help="creates the default application with services based on the default SLA",
        action="store_true",
    )
    applications_create_parser.set_defaults(func=aux_create_application)
