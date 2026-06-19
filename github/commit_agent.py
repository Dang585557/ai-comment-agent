import os
from github import Github
from github.InputGitTreeElement import InputGitTreeElement


class CommitAgent:

    def __init__(self):

        self.client = Github(
            os.getenv("GITHUB_TOKEN")
        )

        self.repo = self.client.get_repo(
            os.getenv("GITHUB_REPOSITORY")
        )

    def latest_commit(self):

        commit = self.repo.get_commits()[0]

        return {

            "sha": commit.sha,

            "message": commit.commit.message,

            "author": commit.commit.author.name

        }

    def create_file(

        self,

        path: str,

        content: str,

        message: str

    ):

        self.repo.create_file(

            path,

            message,

            content,

            branch=self.repo.default_branch

        )

    def update_file(

        self,

        path: str,

        content: str,

        message: str

    ):

        file = self.repo.get_contents(path)

        self.repo.update_file(

            path,

            message,

            content,

            file.sha,

            branch=self.repo.default_branch

        )

    def delete_file(

        self,

        path: str,

        message: str

    ):

        file = self.repo.get_contents(path)

        self.repo.delete_file(

            path,

            message,

            file.sha,

            branch=self.repo.default_branch

        )

    def commit_history(self, limit=20):

        history = []

        for commit in self.repo.get_commits()[:limit]:

            history.append({

                "sha": commit.sha,

                "message": commit.commit.message,

                "author": commit.commit.author.name

            })

        return history

    def health(self):

        return {

            "status": "ONLINE",

            "repository": self.repo.full_name

        }


if __name__ == "__main__":

    agent = CommitAgent()

    print(agent.health())
