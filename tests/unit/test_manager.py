import unittest

from manager.manager import Manager


class TestManager(unittest.TestCase):

    def setUp(self):

        self.manager = Manager()

    def test_manager_created(self):

        self.assertIsNotNone(
            self.manager
        )

    def test_has_dispatch_method(self):

        self.assertTrue(
            hasattr(
                self.manager,
                "dispatch"
            )
        )

    def test_has_schedule_method(self):

        self.assertTrue(
            hasattr(
                self.manager,
                "schedule"
            )
        )


if __name__ == "__main__":

    unittest.main()
