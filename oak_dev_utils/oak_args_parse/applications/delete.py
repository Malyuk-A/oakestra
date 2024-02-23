import argparse
from typing import Any

from oak_dev_utils.applications.delete import delete_all_applications, delete_application
from oak_dev_utils.login import login_and_set_token
from oak_dev_utils.oak_args_parse.types import Subparsers

APP_ID_HELP_TEXT = """
if a (single) application ID is provided only that one app will be deleted
if 'all' is provided every application gets deleted"""

DELETION_HELP_TEXT = "deletes one or all applications" + APP_ID_HELP_TEXT


def prepare_applications_deletion_argparser(applications_subparsers: Subparsers) -> None:
    def aux_delete_appliacations(args: Any):
        if args.app_id == "all":
            delete_all_applications()
        else:
            delete_application(args.app_id)

    applications_deletion_parser = applications_subparsers.add_parser(
        "delete",
        aliases=["d"],
        help=DELETION_HELP_TEXT,
        description=DELETION_HELP_TEXT,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    applications_deletion_parser.add_argument("app_id", type=str, help=APP_ID_HELP_TEXT)
    applications_deletion_parser.set_defaults(func=aux_delete_appliacations)
