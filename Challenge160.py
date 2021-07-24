import unittest


def car_timer(drive_time) -> int:
    time = str(drive_time // 60)  # hours
    time += str(drive_time % 60)  # hours + leftover minutes
    total = 0
    for x in time:
        total += int(x)
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(car_timer(240), 4)

    def test_2(self):
        self.assertEqual(car_timer(808), 14)

    def test_3(self):
        self.assertEqual(car_timer(1439), 19)

    def test_4(self):
        self.assertEqual(car_timer(0), 0)

    def test_5(self):
        self.assertEqual(car_timer(23), 5)

    def test_6(self):
        self.assertEqual(car_timer(8), 8)


if __name__ == "__main__":
    unittest.main()