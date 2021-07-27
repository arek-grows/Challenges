import unittest


def calculate_discount(price: int, discount_percent: int) -> float:
    return round(price - (price * discount_percent / 100), 2)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calculate_discount(100, 75), 25)

    def test_2(self):
        self.assertEqual(calculate_discount(211, 50), 105.5)

    def test_3(self):
        self.assertEqual(calculate_discount(593, 61), 231.27)

    def test_4(self):
        self.assertEqual(calculate_discount(1693, 80), 338.6)

    def test_5(self):
        self.assertEqual(calculate_discount(700, 10), 630)


if __name__ == "__main__":
    unittest.main()