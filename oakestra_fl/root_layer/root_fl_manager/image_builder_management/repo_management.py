from typing import NamedTuple

from github import Github


class RepoDetails(NamedTuple):
    repo_id: str
    latest_short_commit_hash: str


def get_repo_details(repo_name: str) -> RepoDetails:
    github_access = Github()
    repo = github_access.get_repo(repo_name)

    commits = repo.get_commits()
    latest_commit = commits[0]
    latest_commit_hash_short = latest_commit.sha[:7]

    return RepoDetails(str(repo.id), latest_commit_hash_short)
