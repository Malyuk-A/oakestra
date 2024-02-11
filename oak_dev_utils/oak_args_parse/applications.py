import argparse
from typing import Any

from oak_dev_utils.applications import display_current_applications
from oak_dev_utils.oak_args_parse.types import Subparsers

STATUS_HELP_TEXT = "displays the currently available/active applications"


def prepare_applications_status_argparser(applications_subparsers: Subparsers) -> None:
    def aux_display_current_applications(args: Any) -> None:
        display_current_applications(args.token)

    applications_status_parser = applications_subparsers.add_parser(
        "status",
        aliases=["s"],
        help=STATUS_HELP_TEXT,
        description=STATUS_HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    applications_status_parser.set_defaults(func=aux_display_current_applications)


def prepare_applications_argparsers(subparsers: Subparsers) -> None:
    applications_parser = subparsers.add_parser(
        "applications",
        aliases=["a"],
        help="command for application(s) related activities",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    def applications_parser_print_help(_: Any) -> None:
        applications_parser.print_help()

    applications_parser.set_defaults(func=applications_parser_print_help)

    applications_subparsers = applications_parser.add_subparsers(
        dest="applications commands",
    )
    prepare_applications_status_argparser(applications_subparsers)
