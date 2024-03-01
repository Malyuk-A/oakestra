import dependency_management.main as dep_manager
from util.common import CONDA_ENV_FILE, run_in_bash


def handle_pyvision() -> None:
    if not dep_manager.dependency_exists("pyvision") and dep_manager.dependency_exists("gmpy2"):
        run_in_bash(f"sed -i 's/- gmpy2.*/- torchvision/' {CONDA_ENV_FILE}")


def handle_pytorch():
    if dep_manager.dependency_exists("torch"):
        handle_pyvision()
