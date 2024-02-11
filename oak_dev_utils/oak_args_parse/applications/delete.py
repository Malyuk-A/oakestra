import argparse
from typing import Any

from oak_dev_utils.applications.general import delete_application
from oak_dev_utils.oak_args_parse.types import Subparsers

DELETION_HELP_TEXT = """
deletes one or all applications
if a (single) application ID is provided only that one app will be deleted
if 'all' is provided every application gets deleted"""


def prepare_applications_deletion_argparser(applications_subparsers: Subparsers) -> None:
    def aux_delete_appliacations(args: Any):
        if args.delete == "all":
            print("delete ALL")
        else:
            print("testing")

    pass
    # applications_deletion_parser = applications_subparsers.add_parser(add_help=False)
    # applications_deletion_parser.add_argument(
    #     "delete",
    #     aliases=["d"],
    #     type=str,
    #     help=DELETION_HELP_TEXT,
    #     description=DELETION_HELP_TEXT,
    #     formatter_class=argparse.RawTextHelpFormatter,
    # )
    # applications_deletion_parser.set_defaults(func=aux_delete_appliacations)
