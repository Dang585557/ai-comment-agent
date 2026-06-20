import unittest
from pathlib import Path


class TestSystem(unittest.TestCase):

    def test_required_directories_exist(self):

        directories = [
            "ceo",
            "manager",
            "dashboard",
            "agents",
            "workflows",
            "llm",
            "memory",
            "computer_control",
            "mobile_lab",
            "github",
            "database",
            "storage",
            "monitoring",
            "logs",
            "configs",
            "tests"
        ]

        for directory in directories:

            self.assertTrue(
                Path(directory).exists(),
                f"{directory} does not exist"
            )

    def test_environment_file_exists(self):

        self.assertTrue(
            Path(".env").exists()
        )

    def test_requirements_exists(self):

        self.assertTrue(
            Path("requirements.txt").exists()
        )

    def test_readme_exists(self):

        self.assertTrue(
            Path("README.md").exists()
        )


if __name__ == "__main__":

    unittest.main()
