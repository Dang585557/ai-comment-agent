import unittest

from dashboard.backend.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):

        self.database = Database()

    def test_database_created(self):

        self.assertIsNotNone(
            self.database
        )

    def test_has_connect_method(self):

        self.assertTrue(
            hasattr(
                self.database,
                "connect"
            )
        )

    def test_has_disconnect_method(self):

        self.assertTrue(
            hasattr(
                self.database,
                "disconnect"
            )
        )

    def test_has_execute_method(self):

        self.assertTrue(
            hasattr(
                self.database,
                "execute"
            )
        )


if __name__ == "__main__":

    unittest.main()
