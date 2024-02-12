from oak_dev_utils.util.common import CustomEnum


class KnownSLA(CustomEnum):
    DEFAULT = "default_app_with_services"
    BLANK = "blank_app_without_services"
    FL = "fl_app"
