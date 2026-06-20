import unittest

from dashboard.backend.api import app


class TestDashboard(unittest.TestCase):

    def test_app_exists(self):

        self.assertIsNotNone(
            app
        )

    def test_app_has_routes(self):

        self.assertGreater(
            len(app.routes),
            0
        )

    def test_app_title(self):

        self.assertIsInstance(
            app.title,
            str
        )


if __name__ == "__main__":

    unittest.main()
