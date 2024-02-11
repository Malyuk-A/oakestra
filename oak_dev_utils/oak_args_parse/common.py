# PYTHON_ARGCOMPLETE_OK

import argparse

import argcomplete

from oak_dev_utils.login import login_and_get_token
from oak_dev_utils.oak_args_parse.applications import prepare_applications_argparsers


def parse_arguments_and_execute() -> None:
    parser = argparse.ArgumentParser()

    # 'dest' & 'required' are needed to ensure correct behavior if no arguments are passed.
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    prepare_applications_argparsers(subparsers)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    bearer_auth_token = login_and_get_token()
    args.token = bearer_auth_token
    args.func(args)
