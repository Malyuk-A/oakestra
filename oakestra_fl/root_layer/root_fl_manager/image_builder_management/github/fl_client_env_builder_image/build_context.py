import git

_build_context = None


class BuildContext:
    def __init__(
        self,
        repo_url: str,
        image_registry_url: str,
        service_id: str,
        mqtt_url: str,
        mqtt_port: str,
        builder_app_name: str,
    ):
        self.repo_url = repo_url
        self.image_registry_url = image_registry_url
        self.mqtt_url = mqtt_url
        self.mqtt_port = mqtt_port
        self.service_id = service_id
        self.builder_app_name = builder_app_name

        self.cloned_repo = None
        self.new_image_name_with_tag = None

        global _build_context
        _build_context = self

    def set_cloned_repo(self, cloned_repo: git.repo.base.Repo) -> None:
        self.cloned_repo = cloned_repo

    def set_new_image_name_with_tag(self, new_image_name_with_tag: str) -> None:
        self.new_image_name_with_tag = new_image_name_with_tag


def get_build_context() -> BuildContext:
    return _build_context
