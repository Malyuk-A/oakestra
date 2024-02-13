#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

from oak_dev_utils.login import login_and_set_token
from oak_dev_utils.oak_args_parse.main import parse_arguments_and_execute


def main():
    login_and_set_token()
    parse_arguments_and_execute()


if __name__ == "__main__":
    main()
