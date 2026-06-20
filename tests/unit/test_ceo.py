import unittest

from ceo.command_center import CommandCenter


class TestCEO(unittest.TestCase):

    def setUp(self):

        self.command_center = CommandCenter()

    def test_command_center_exists(self):

        self.assertIsNotNone(
            self.command_center
        )

    def test_has_execute_method(self):

        self.assertTrue(
            hasattr(
                self.command_center,
                "execute"
            )
        )

    def test_has_status_method(self):

        self.assertTrue(
            hasattr(
                self.command_center,
                "status"
            )
        )


if __name__ == "__main__":

    unittest.main()
