import os
from github import Github


class GitHubAgent:

    def __init__(self):

        self.token = os.getenv("GITHUB_TOKEN")

        self.repo_name = os.getenv("GITHUB_REPOSITORY")

        self.client = Github(self.token)

        self.repo = self.client.get_repo(self.repo_name)

    def repository(self):

        return {

            "name": self.repo.full_name,

            "branch": self.repo.default_branch,

            "stars": self.repo.stargazers_count,

            "private": self.repo.private

        }

    def branches(self):

        return [

            branch.name

            for branch in self.repo.get_branches()

        ]

    def commits(self, limit=10):

        commits = []

        for commit in self.repo.get_commits()[:limit]:

            commits.append({

                "sha": commit.sha,

                "message": commit.commit.message,

                "author": commit.commit.author.name

            })

        return commits

    def create_issue(self, title, body):

        issue = self.repo.create_issue(

            title=title,

            body=body

        )

        return issue.html_url

    def pull_requests(self):

        return [

            {

                "title": pr.title,

                "number": pr.number,

                "state": pr.state

            }

            for pr in self.repo.get_pulls()

        ]

    def health(self):

        return {

            "status": "ONLINE",

            "repository": self.repo.full_name

        }


if __name__ == "__main__":

    github = GitHubAgent()

    print(github.health())
