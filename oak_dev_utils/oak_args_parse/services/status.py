import argparse
from typing import Any

from oak_dev_utils.login import login_and_set_token
from oak_dev_utils.oak_args_parse.types import Subparsers
from oak_dev_utils.services.get import get_single_service
from oak_dev_utils.services.status import display_all_current_services, disply_single_service


def aux_display_current_services(args: Any) -> None:
    if args.all or args.appid:
        display_all_current_services(verbose=args.verbose, app_id=args.appid)
    elif args.serviceid:
        service = get_single_service(args.serviceid)
        disply_single_service(service, verbose=args.verbose)


def prepare_services_display_argparser(services_subparsers: Subparsers) -> None:
    HELP_TEXT = "displays the currently available/active service(s)"
    services_status_parser = services_subparsers.add_parser(
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
        "--appid",
        type=str,
    )
    services_status_parser.add_argument(
        "--serviceid",
        "-i",
        type=str,
    )
    services_status_parser.set_defaults(func=aux_display_current_services)
