from oak_dev_utils.services.get import get_all_services
from oak_dev_utils.util.dev_logger import dev_logger


def log_aux(key: str, value: str) -> None:
    dev_logger.info(f"   {key}: '{value}'")


def verbose_log_aux(section_name: str) -> None:
    dev_logger.info(f"   - {section_name} -")


def display_all_current_services(verbose: bool = False, app_id: str = None) -> None:
    all_current_services = get_all_services(app_id)

    dev_logger.info(f"All current services: '{len(all_current_services)}'")
    for i, service in enumerate(all_current_services):
        dev_logger.info(f" Service '{i}':")

        verbose_log_aux("microservice")
        log_aux("id", service["microserviceID"])
        log_aux("microservice name" if verbose else "name", service["microservice_name"])
        log_aux("microservice ns" if verbose else "ns", service["microservice_namespace"])
        if app_id is None:
            log_aux("parent app", f"{service['app_name']}: {service['applicationID']}")

        if verbose:
            verbose_log_aux("service")
            log_aux("service name", service["service_name"])

        verbose_log_aux("resources")
        log_aux("memory", service["memory"])
        log_aux("vcpus", service["vcpus"])
        if verbose:
            log_aux("storage", service["storage"])
            log_aux("vgpus", service["vgpus"])

        verbose_log_aux("container")
        log_aux("image", service["image"])
        if verbose:
            log_aux("code", service["code"])

        verbose_log_aux("networking")
        log_aux("port", service["port"])
        if verbose:
            log_aux("bandwidth in", service["bandwidth_in"])
            log_aux("bandwidth out", service["bandwidth_out"])

        verbose_log_aux("instances")
        log_aux("instances", service["instance_list"])
