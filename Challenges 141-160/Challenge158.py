import unittest


def time_saved(speed_limit: int, average_speed: int, distance: int) -> float:
    slimit_time = distance / speed_limit * 60
    actual_time = distance / average_speed * 60
    return round(slimit_time - actual_time, 1)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_(self):
        self.assertEqual(time_saved(80, 90, 40), 3.3)

    def test_1(self):
        self.assertEqual(time_saved(80, 90, 4000), 333.3)

    def test_2(self):
        self.assertEqual(time_saved(80, 100, 40), 6.0)

    def test_3(self):
        self.assertEqual(time_saved(80, 100, 10), 1.5)

    def test_4(self):
        self.assertEqual(time_saved(60, 65, 25), 1.9)

    def test_5(self):
        self.assertEqual(time_saved(60, 60, 20), 0)

    def test_6(self):
        self.assertEqual(time_saved(80, 95, 200), 23.7)

    def test_7(self):
        self.assertEqual(time_saved(70, 92, 50), 10.2)

    def test_8(self):
        self.assertEqual(time_saved(70, 92, 20), 4.1)

    def test_9(self):
        self.assertEqual(time_saved(70, 100, 12), 3.1)


if __name__ == "__main__":
    unittest.main()