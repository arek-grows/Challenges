import unittest


def wash_hands(times_daily: int, total_months: int) -> str:
    total_seconds = times_daily * total_months * 30 * 21
    total_minutes = int(total_seconds/60)
    seconds_remainder = total_seconds % 60
    return "%s minutes and %s seconds" %(total_minutes, seconds_remainder)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wash_hands(8, 7), "588 minutes and 0 seconds")

    def test_2(self):
        self.assertEqual(wash_hands(20, 10), "2100 minutes and 0 seconds")

    def test_3(self):
        self.assertEqual(wash_hands(7, 9), "661 minutes and 30 seconds")

    def test_4(self):
        self.assertEqual(wash_hands(0, 2), "0 minutes and 0 seconds")

    def test_5(self):
        self.assertEqual(wash_hands(13, 3), "409 minutes and 30 seconds")

    def test_6(self):
        self.assertEqual(wash_hands(1, 1), "10 minutes and 30 seconds")

    def test_7(self):
        self.assertEqual(wash_hands(7, 0), "0 minutes and 0 seconds")


if __name__ == "__main__":
    unittest.main()