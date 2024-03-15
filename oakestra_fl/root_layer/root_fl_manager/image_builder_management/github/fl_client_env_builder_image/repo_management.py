import errno
import os
import shutil

import git
from dependency_management.main import handle_dependencies
from utils.common import CLONED_REPO_PATH, CONDA_ENV_FILE_PATH, FL_ENV_PATH, run_in_bash
from utils.logging import logger


def clone_repo(repo_url: str) -> git.repo.base.Repo:
    repo = git.Repo.clone_from(repo_url, str(CLONED_REPO_PATH))
    return repo


def _check_conda_env_name() -> None:
    run_in_bash(f"sed -i -e 's/name: mlflow-env/name: base/' {CONDA_ENV_FILE_PATH}")


def _copy_verified_repo_content_into_fl_env() -> None:
    for item in CLONED_REPO_PATH.iterdir():
        src = item
        dst = FL_ENV_PATH / item.name
        if src.is_file():
            shutil.copy2(src, dst)
        elif src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)


# Note: Further checks can be added here, e.g.:
# - if the conda dependencies make sense, are valid
# - maybe even "adjust/augment" them here
# - check if any maliciouse code is included in this repo
# -- to avoid running this code in on the worker node.
def check_cloned_repo(cloned_repo: git.repo.base.Repo) -> None:
    root_tree = cloned_repo.tree()

    files_to_check = ["client.py", CONDA_ENV_FILE_PATH.name]
    for file in files_to_check:
        if file not in [blob.name for blob in root_tree.blobs]:
            logger.critical(f"{file} not found in the cloned repository.")
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
        else:
            logger.debug(f"{file} found in the repository.")

    _check_conda_env_name()
    handle_dependencies()
    _copy_verified_repo_content_into_fl_env()
