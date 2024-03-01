from dependency_management.pytorch import handle_pytorch
from util.common import CONDA_ENV_FILE, run_in_bash


def dependency_exists(target_dependency: str) -> bool:
    bash_cmd = f"grep '{target_dependency}' {CONDA_ENV_FILE}"
    # Hint: success = returncode == 0 -> bool = false
    #       failure = returncode != 0 -> bool = true
    # -> needs to be inverted
    return not bool(run_in_bash(bash_cmd).returncode)


def handle_dependencies():
    handle_pytorch()
