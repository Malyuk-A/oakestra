import requests

from oak_dev_utils.services.get import get_single_service
from oak_dev_utils.util.api import check_api_response, create_api_query


def deploy_new_instance(service_id: str):
    url, headers, _ = create_api_query(f"/api/service/{service_id}/instance")
    response = requests.post(url, headers=headers)
    check_api_response(
        response,
        what_should_happen=(f"Deploy a new instance for the service '{service_id}'"),
    )


def undeploy_instance(service_id: str, instance_id: str):
    url, headers, _ = create_api_query(f"/api/service/{service_id}/instance/{instance_id}")
    response = requests.delete(url, headers=headers)
    check_api_response(
        response,
        what_should_happen=(f"Undeploy instance '{instance_id}' for the service '{service_id}'"),
    )


def undeploy_all_instances_of_service(service_id: str):
    service = get_single_service(service_id)
    for instance in service["instance_list"]:
        undeploy_instance(service_id, instance["instance_number"])
