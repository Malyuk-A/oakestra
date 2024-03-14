from http import HTTPStatus
from typing import Optional, Tuple

from api.utils import handle_request


def get_latest_commit_hash(repo_name: str) -> Tuple[HTTPStatus, Optional[str]]:

    core_git_api_endpoint = f"/repos/{repo_name}/commits"
    main_git_api_endpoint = f"{core_git_api_endpoint}/main"

    status, json_data = handle_request(
        base_url="https://api.github.com",
        what_should_happen="Fetch commits from github",
        api_endpoint=main_git_api_endpoint,
    )
    if status != HTTPStatus.OK:
        return status, None

    # Note: Cut down the long hash to the usual short one for readability.
    return status, json_data["sha"][:7]
