# PYTHON_ARGCOMPLETE_OK

import argparse

import argcomplete

from oak_dev_utils.oak_args_parse.applications.main import prepare_applications_argparsers
from oak_dev_utils.oak_args_parse.docker.main import prepare_docker_argparsers
from oak_dev_utils.oak_args_parse.services.main import prepare_services_argparsers


def parse_arguments_and_execute() -> None:
    parser = argparse.ArgumentParser()

    # 'dest' & 'required' are needed to ensure correct behavior if no arguments are passed.
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    prepare_applications_argparsers(subparsers)
    prepare_services_argparsers(subparsers)
    prepare_docker_argparsers(subparsers)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    args.func(args)
