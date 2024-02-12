from oak_dev_utils.services.get import get_all_services
from oak_dev_utils.util.dev_logger import dev_logger


def log_aux_service(key: str, value: str, service) -> None:
    value = service.get(value, None)
    if value is not None:
        log_aux(key, value)


def log_aux(key: str, value: str) -> None:
    dev_logger.info(f"   {key}: '{value}'")


def verbose_log_aux(section_name: str) -> None:
    dev_logger.info(f"   - {section_name} -")


def disply_single_service(service, verbose: bool = False) -> None:
    verbose_log_aux("microservice")
    log_aux_service("id", "microserviceID", service)
    log_aux_service("microservice name" if verbose else "name", "microservice_name", service)
    log_aux_service("microservice ns" if verbose else "ns", "microservice_namespace", service)
    log_aux("parent app", f"{service['app_name']}: {service['applicationID']}")

    if verbose:
        verbose_log_aux("service")
        log_aux_service("service name", "service_name", service)

    verbose_log_aux("resources")
    log_aux_service("memory", "memory", service)
    log_aux_service("vcpus", "vcpus", service)
    if verbose:
        log_aux_service("storage", "storage", service)
        log_aux_service("vgpus", "vgpus", service)

    verbose_log_aux("container")
    log_aux_service("image", "image", service)
    if verbose:
        log_aux_service("code", "code", service)

    verbose_log_aux("networking")
    log_aux_service("port", "port", service)
    if verbose:
        log_aux_service("bandwidth in", "bandwidth_in", service)
        log_aux_service("bandwidth out", "bandwidth_out", service)

    verbose_log_aux("instances")
    instances = service["instance_list"]
    num_instances = len(instances)
    log_aux("instances", num_instances)
    if verbose and num_instances > 0:
        for i, instance in enumerate(instances):
            dev_logger.info(f"   Instance '{i}':")
            log_aux("  instance_number", instance["instance_number"])
            log_aux("  status", instance["status"])
            log_aux("  publicip", instance["publicip"])
            log_aux("  cpu", instance["cpu"])


def display_all_current_services(verbose: bool = False, app_id: str = None) -> None:
    all_current_services = get_all_services(app_id)

    dev_logger.info(f"All current services: '{len(all_current_services)}'")
    for i, service in enumerate(all_current_services):
        dev_logger.info(f" Service '{i}':")
        disply_single_service(service, verbose)
