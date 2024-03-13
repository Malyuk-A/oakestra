import json

from image_registry.common import ROOT_FL_IMAGE_REGISTRY_URL
from utils.common import FLOPS_USER_ACCOUNT, ROOT_FL_MANAGER_IP, ROOT_FL_MANAGER_PORT
from utils.types import JSON_SLA


def generate_builder_sla(
    repo_url: str,
    repo_id: str,
    latest_short_commit_hash: str,
    service_id: str,
) -> JSON_SLA:
    return json.dumps(
        {
            "sla_version": "v2.0",
            "customerID": FLOPS_USER_ACCOUNT,
            "applications": [
                {
                    "applicationID": "",
                    "application_name": f"{repo_id[0]}{latest_short_commit_hash}",
                    "application_namespace": "fl-build",
                    "application_desc": "fl_plugin application for building FL client env images",
                    "microservices": [
                        {
                            "microserviceID": "",
                            "microservice_name": "builder",
                            "microservice_namespace": "fl-build",
                            "virtualization": "container",
                            "one_shot": True,
                            "cmd": [
                                "python3",
                                "main.py",
                                repo_url,
                                ROOT_FL_IMAGE_REGISTRY_URL,
                                service_id,
                                ROOT_FL_MANAGER_IP,
                                ROOT_FL_MANAGER_PORT,
                            ],
                            "memory": 2000,
                            "vcpus": 1,
                            "storage": 15,
                            "image": "ghcr.io/malyuk-a/fl-client-env-builder:latest",
                        }
                    ],
                }
            ],
        }
    )
