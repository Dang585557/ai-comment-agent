import unittest

from agents.tiktok.manager import TikTokManager
from agents.video.editor_agent import EditorAgent
from agents.developer.architect_agent import ArchitectAgent
from agents.research.competitor_agent import CompetitorAgent
from agents.website.deploy_agent import DeployAgent


class TestAgents(unittest.TestCase):

    def test_tiktok_manager(self):

        manager = TikTokManager()

        self.assertIsNotNone(manager)

    def test_video_agent(self):

        agent = EditorAgent()

        self.assertIsNotNone(agent)

    def test_developer_agent(self):

        agent = ArchitectAgent()

        self.assertIsNotNone(agent)

    def test_research_agent(self):

        agent = CompetitorAgent()

        self.assertIsNotNone(agent)

    def test_website_agent(self):

        agent = DeployAgent()

        self.assertIsNotNone(agent)


if __name__ == "__main__":

    unittest.main()
