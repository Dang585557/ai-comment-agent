import os
from github import Github


class ReleaseAgent:

    def __init__(self):

        self.client = Github(
            os.getenv("GITHUB_TOKEN")
        )

        self.repo = self.client.get_repo(
            os.getenv("GITHUB_REPOSITORY")
        )

    def list_releases(self):

        releases = []

        for release in self.repo.get_releases():

            releases.append({

                "id": release.id,

                "tag": release.tag_name,

                "title": release.title,

                "draft": release.draft,

                "prerelease": release.prerelease,

                "published_at": str(release.published_at)

            })

        return releases

    def latest_release(self):

        release = self.repo.get_latest_release()

        return {

            "tag": release.tag_name,

            "title": release.title,

            "url": release.html_url

        }

    def create_release(

        self,

        tag: str,

        title: str,

        body: str,

        draft=False,

        prerelease=False

    ):

        release = self.repo.create_git_release(

            tag=tag,

            name=title,

            message=body,

            draft=draft,

            prerelease=prerelease

        )

        return release.html_url

    def delete_release(self, release_id):

        release = self.repo.get_release(release_id)

        release.delete_release()

        return True

    def health(self):

        return {

            "status": "ONLINE",

            "repository": self.repo.full_name

        }


if __name__ == "__main__":

    agent = ReleaseAgent()

    print(agent.health())
