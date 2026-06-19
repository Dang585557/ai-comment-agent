import os
from github import Github
from github.GithubException import GithubException


class BranchAgent:

    def __init__(self):

        self.client = Github(
            os.getenv("GITHUB_TOKEN")
        )

        self.repo = self.client.get_repo(
            os.getenv("GITHUB_REPOSITORY")
        )

    def list_branches(self):

        return [

            branch.name

            for branch in self.repo.get_branches()

        ]

    def create_branch(self, name: str):

        source = self.repo.get_branch(
            self.repo.default_branch
        )

        self.repo.create_git_ref(
            ref=f"refs/heads/{name}",
            sha=source.commit.sha
        )

        return True

    def delete_branch(self, name: str):

        ref = self.repo.get_git_ref(
            f"heads/{name}"
        )

        ref.delete()

        return True

    def branch_exists(self, name: str):

        try:

            self.repo.get_branch(name)

            return True

        except GithubException:

            return False

    def default_branch(self):

        return self.repo.default_branch

    def health(self):

        return {

            "status": "ONLINE",

            "repository": self.repo.full_name,

            "default_branch": self.repo.default_branch

        }


if __name__ == "__main__":

    agent = BranchAgent()

    print(agent.health())
