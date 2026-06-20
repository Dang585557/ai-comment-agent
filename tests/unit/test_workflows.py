import unittest
from pathlib import Path
import yaml


class TestWorkflows(unittest.TestCase):

    def test_daily_report_exists(self):

        self.assertTrue(
            Path(
                "workflows/daily_report.yaml"
            ).exists()
        )

    def test_content_creation_exists(self):

        self.assertTrue(
            Path(
                "workflows/content_creation.yaml"
            ).exists()
        )

    def test_video_pipeline_exists(self):

        self.assertTrue(
            Path(
                "workflows/video_pipeline.yaml"
            ).exists()
        )

    def test_yaml_is_valid(self):

        files = [
            "workflows/daily_report.yaml",
            "workflows/content_creation.yaml",
            "workflows/video_pipeline.yaml",
            "workflows/research_pipeline.yaml",
            "workflows/website_pipeline.yaml",
            "workflows/expansion_pipeline.yaml",
        ]

        for file in files:

            with open(file, "r", encoding="utf-8") as f:

                data = yaml.safe_load(f)

                self.assertIsNotNone(data)


if __name__ == "__main__":

    unittest.main()
