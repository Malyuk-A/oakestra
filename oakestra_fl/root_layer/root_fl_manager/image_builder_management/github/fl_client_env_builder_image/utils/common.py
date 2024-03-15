import pathlib
import shlex
import subprocess

FL_CLIENT_ENV_IMAGE_PATH = pathlib.Path("fl_client_env_image")
CLONED_REPO_PATH = FL_CLIENT_ENV_IMAGE_PATH / "cloned_repo"
FL_ENV_PATH = FL_CLIENT_ENV_IMAGE_PATH / "fl_env"
CONDA_ENV_FILE_PATH = CLONED_REPO_PATH / "conda.yaml"


def run_in_bash(bash_cmd: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(shlex.split(bash_cmd), capture_output=True)
