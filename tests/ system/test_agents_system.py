import unittest
from agents.tiktok.manager import TikTokManager
from agents.video.editor_agent import EditorAgent
from agents.developer.architect_agent import ArchitectAgent
from agents.research.competitor_agent import CompetitorAgent
from agents.website.deploy_agent import DeployAgent
class TestAgentsSystem(unittest.TestCase):

    def test_initialize_all_agents(self):

        agents = [
            TikTokManager(),
            EditorAgent(),
            ArchitectAgent(),
            CompetitorAgent(),
            DeployAgent()
        ]

        self.assertEqual(
            len(agents),
            5
        )

    def test_agents_are_available(self):

        self.assertIsNotNone(
            TikTokManager()
        )

        self.assertIsNotNone(
            EditorAgent()
        )

        self.assertIsNotNone(
            ArchitectAgent()
        )

        self.assertIsNotNone(
            CompetitorAgent()
        )

        self.assertIsNotNone(
            DeployAgent()
        )


if __name__ == "__main__":

    unittest.main()
