import unittest


def cars(wheels: int, car_bodies: int, figures: int) -> int:
    return min([wheels//4, car_bodies//1, figures//2])  # Put your code here!!!


class TestCars(unittest.TestCase):
    def test_1(self):
        self.assertEqual(9, cars(37, 15, 20))

    def test_2(self):
        self.assertEqual(7, cars(72, 7, 21))

    def test_3(self):
        self.assertEqual(2, cars(9, 44, 34))

    def test_4(self):
        self.assertEqual(3, cars(50, 38, 7))

    def test_5(self):
        self.assertEqual(9, cars(68, 9, 44))

    def test_6(self):
        self.assertEqual(0, cars(3, 29, 54))

    def test_7(self):
        self.assertEqual(7, cars(28, 34, 80))

    def test_8(self):
        self.assertEqual(22, cars(88, 50, 83))

    def test_9(self):
        self.assertEqual(10, cars(66, 18, 21))

    def test_10(self):
        self.assertEqual(5, cars(97, 6, 10))


if __name__ == "__main__":
    unittest.main()