import os
from github import Github


class RepositoryManager:

    def __init__(self):

        self.client = Github(
            os.getenv("GITHUB_TOKEN")
        )

        self.repo = self.client.get_repo(
            os.getenv("GITHUB_REPOSITORY")
        )

    def info(self):

        return {

            "name": self.repo.name,

            "full_name": self.repo.full_name,

            "private": self.repo.private,

            "default_branch": self.repo.default_branch,

            "description": self.repo.description,

            "stars": self.repo.stargazers_count,

            "forks": self.repo.forks_count,

            "open_issues": self.repo.open_issues_count

        }

    def contributors(self):

        return [

            {

                "login": user.login,

                "contributions": user.contributions

            }

            for user in self.repo.get_contributors()

        ]

    def languages(self):

        return self.repo.get_languages()

    def tags(self):

        return [

            tag.name

            for tag in self.repo.get_tags()

        ]

    def topics(self):

        return self.repo.get_topics()

    def set_topics(self, topics):

        self.repo.replace_topics(topics)

    def clone_url(self):

        return self.repo.clone_url

    def ssh_url(self):

        return self.repo.ssh_url

    def html_url(self):

        return self.repo.html_url

    def health(self):

        return {

            "status": "ONLINE",

            "repository": self.repo.full_name,

            "branch": self.repo.default_branch

        }


if __name__ == "__main__":

    manager = RepositoryManager()

    print(manager.health())
