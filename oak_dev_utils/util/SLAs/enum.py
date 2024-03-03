from oak_dev_utils.util.common import CustomEnum


class KnownSLA(CustomEnum):
    DEFAULT = "default_app_with_services"
    BLANK = "blank_app_without_services"
    FL = "fl_app"
    BUILDER = "fl_client_env_builder"
    ENDLESS_BUILDER = "endless_builder"
    ENDLESS_CONDA = "endless_conda"
