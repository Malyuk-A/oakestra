import errno
import os
import pathlib

import git
from util_logging import logger

CLONED_REPO_PATH = pathlib.Path("/cloned_repo")


def clone_repo(repo_url: str) -> git.repo.base.Repo:
    repo = git.Repo.clone_from(repo_url, str(CLONED_REPO_PATH))
    return repo


# Note: Further checks can be added here, e.g.:
# - if the conda dependencies make sense, are valid
# - maybe even "adjust/augment" them here
# - check if any maliciouse code is included in this repo
# -- to avoid running this code in on the worker node.
def check_cloned_repo(cloned_repo: git.repo.base.Repo) -> None:
    root_tree = cloned_repo.tree()

    files_to_check = ["client.py", "conda.yaml"]
    for file in files_to_check:
        if file not in [blob.name for blob in root_tree.blobs]:
            logger.critical(f"{file} not found in the cloned repository.")
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
        else:
            logger.debug(f"{file} found in the repository.")
