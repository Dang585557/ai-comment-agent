import unittest
from pathlib import Path


class TestProjectStructure(unittest.TestCase):

    def test_core_directories(self):

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

            with self.subTest(directory=directory):

                self.assertTrue(
                    Path(directory).is_dir()
                )

    def test_core_files(self):

        files = [
            "README.md",
            "requirements.txt",
            ".env",
            "docker-compose.yml"
        ]

        for file in files:

            with self.subTest(file=file):

                self.assertTrue(
                    Path(file).exists()
                )


if __name__ == "__main__":

    unittest.main()
