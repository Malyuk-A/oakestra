import os
import pathlib

from utils.common import run_in_bash

CAROOT_PATH = pathlib.Path(os.environ.get("CAROOT"))

CA_KEY_PATH = CAROOT_PATH / "rootCA-key.pem"
CA_CERT_PATH = CAROOT_PATH / "rootCA.pem"

REGISTRY_KEY_PATH = CAROOT_PATH / "registry-key.pem"
REGISTRY_CERT_PATH = CAROOT_PATH / "registry.pem"


def handle_ca_and_certificates():
    if not CA_KEY_PATH.exists() or not CA_CERT_PATH.exists():
        run_in_bash("mkcert -install")
    if not REGISTRY_KEY_PATH.exists() or not REGISTRY_CERT_PATH.exists():
        run_in_bash(
            " ".join(
                (
                    "mkcert",
                    f"-cert-file {CAROOT_PATH}/registry.pem",
                    f"-key-file {CAROOT_PATH}/registry-key.pem",
                    "192.168.178.44",
                    "localhost",
                )
            )
        )
