import unittest

from counter_service import CounterService


class CounterServiceTests(unittest.TestCase):
    def test_get_current_value_returns_two_after_two_increments(self) -> None:
        service = CounterService()

        service.increment()
        service.increment()

        self.assertEqual(service.get_current_value(), 2)


if __name__ == "__main__":
    unittest.main()
