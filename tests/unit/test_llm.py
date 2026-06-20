import unittest

from llm.router import LLMRouter


class TestLLM(unittest.TestCase):

    def setUp(self):

        self.router = LLMRouter()

    def test_router_created(self):

        self.assertIsNotNone(
            self.router
        )

    def test_available_models(self):

        models = self.router.available_models()

        self.assertIsInstance(
            models,
            list
        )

        self.assertGreater(
            len(models),
            0
        )

    def test_get_openai_client(self):

        client = self.router.get_client(
            "openai"
        )

        self.assertIsNotNone(
            client
        )


if __name__ == "__main__":

    unittest.main()
