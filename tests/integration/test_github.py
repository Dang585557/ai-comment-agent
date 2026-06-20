import unittest

from github.github_agent import GitHubAgent


class TestGitHub(unittest.TestCase):

    def setUp(self):

        self.agent = GitHubAgent()

    def test_agent_created(self):

        self.assertIsNotNone(
            self.agent
        )

    def test_has_connect_method(self):

        self.assertTrue(
            hasattr(
                self.agent,
                "connect"
            )
        )

    def test_has_repository_method(self):

        self.assertTrue(
            hasattr(
                self.agent,
                "get_repository"
            )
        )

    def test_has_commit_method(self):

        self.assertTrue(
            hasattr(
                self.agent,
                "commit"
            )
        )


if __name__ == "__main__":

    unittest.main()
