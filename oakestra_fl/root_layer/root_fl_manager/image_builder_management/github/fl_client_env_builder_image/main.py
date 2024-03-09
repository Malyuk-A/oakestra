from image_management import (
    build_repo_specific_fl_client_env_image,
    prepare_and_resolve_dependencies,
    prepare_new_image_name_with_tag,
    push_image,
)
from mqtt import notify_root_fl_manager
from repo_management import check_cloned_repo, clone_repo
from util.arg_parsing import parse_args


def main() -> None:
    (
        repo_url,
        image_registry_url,
        service_id,
        mqtt_url,
        mqtt_port,
    ) = parse_args()

    cloned_repo = clone_repo(repo_url)
    check_cloned_repo(cloned_repo)
    image_name_with_tag = prepare_new_image_name_with_tag(cloned_repo, image_registry_url)

    prepare_and_resolve_dependencies()

    build_repo_specific_fl_client_env_image(image_name_with_tag)
    push_image(image_name_with_tag)

    # TODO: Add error handling if build fails - should notify RFLM about this
    # notify_root_fl_manager(mqtt_url, mqtt_port, service_id, image_name_with_tag)


if __name__ == "__main__":
    main()
