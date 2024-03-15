from image_management import (
    build_repo_specific_fl_client_env_image,
    prepare_new_image_name_with_tag,
    push_image,
)
from notification_management import (
    notify_about_failed_build_and_terminate,
    notify_about_successful_build,
)
from repo_management import check_cloned_repo, clone_repo
from utils.arg_parsing import parse_args


def main() -> None:
    parse_args()
    try:
        clone_repo()
        check_cloned_repo()

        prepare_new_image_name_with_tag()
        build_repo_specific_fl_client_env_image()
        push_image()

        notify_about_successful_build()
    except Exception as e:
        notify_about_failed_build_and_terminate(f"Something unexpected went wrong; '{e}'")


if __name__ == "__main__":
    main()
