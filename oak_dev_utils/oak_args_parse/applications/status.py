import argparse
from typing import Any

from oak_dev_utils.applications.status import display_current_applications
from oak_dev_utils.login import login_and_set_token
from oak_dev_utils.oak_args_parse.types import Subparsers


def prepare_applications_display_argparser(applications_subparsers: Subparsers) -> None:
    def aux_display_current_applications(args: Any):
        login_and_set_token()
        display_current_applications()

    HELP_TEXT = "displays the currently available/active applications"
    applications_status_parser = applications_subparsers.add_parser(
        "status",
        aliases=["s"],
        help=HELP_TEXT,
        description=HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    applications_status_parser.set_defaults(func=aux_display_current_applications)
