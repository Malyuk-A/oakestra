import argparse
from typing import Any

from oak_dev_utils.oak_args_parse.types import Subparsers
from oak_dev_utils.services.status import display_all_current_services


def aux_display_current_services(args: Any) -> None:
    display_all_current_services(verbose=args.verbose, app_id=args.id)


def prepare_services_display_argparser(applications_subparsers: Subparsers) -> None:
    HELP_TEXT = "displays the currently available/active service(s)"
    services_status_parser = applications_subparsers.add_parser(
        "status",
        aliases=["s"],
        help=HELP_TEXT,
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    services_status_parser.add_argument(
        "-a",
        "--all",
        help="displays all services",
        action="store_true",
    )
    services_status_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
    )
    services_status_parser.add_argument(
        "--id",
        "-i",
        type=str,
    )
    services_status_parser.set_defaults(func=aux_display_current_services)
