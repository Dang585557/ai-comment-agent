import unittest

from fastapi.testclient import TestClient

from dashboard.backend.api import app


class TestAPI(unittest.TestCase):

    def setUp(self):

        self.client = TestClient(app)

    def test_root_endpoint(self):

        response = self.client.get("/")

        self.assertIn(
            response.status_code,
            [200, 404]
        )

    def test_docs_endpoint(self):

        response = self.client.get("/docs")

        self.assertEqual(
            response.status_code,
            200
        )

    def test_openapi_endpoint(self):

        response = self.client.get("/openapi.json")

        self.assertEqual(
            response.status_code,
            200
        )


if __name__ == "__main__":

    unittest.main()
