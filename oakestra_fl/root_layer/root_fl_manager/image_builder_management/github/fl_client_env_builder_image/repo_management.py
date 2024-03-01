import errno
import os
import pathlib

import git
from dependency_management.main import handle_dependencies
from util.common import CONDA_ENV_FILE, run_in_bash
from util.logging import logger

CLONED_REPO_PATH = pathlib.Path("fl_client_env_image/cloned_repo")


def clone_repo(repo_url: str) -> git.repo.base.Repo:
    repo = git.Repo.clone_from(repo_url, str(CLONED_REPO_PATH))
    return repo


def check_conda_env_name() -> None:
    run_in_bash(f"sed -i -e 's/name: mlflow-env/name: base/' {CONDA_ENV_FILE}")


# Note: Further checks can be added here, e.g.:
# - if the conda dependencies make sense, are valid
# - maybe even "adjust/augment" them here
# - check if any maliciouse code is included in this repo
# -- to avoid running this code in on the worker node.
def check_cloned_repo(cloned_repo: git.repo.base.Repo) -> None:
    root_tree = cloned_repo.tree()

    files_to_check = ["client.py", CONDA_ENV_FILE]
    for file in files_to_check:
        if file not in [blob.name for blob in root_tree.blobs]:
            logger.critical(f"{file} not found in the cloned repository.")
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
        else:
            logger.debug(f"{file} found in the repository.")

    check_conda_env_name()
    handle_dependencies()
