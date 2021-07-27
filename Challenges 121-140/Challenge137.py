import unittest
import math


def factor_group(num: int) -> str:
    if math.sqrt(num).is_integer():
        return "odd"
    return "even"  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("even", factor_group(33))

    def test_2(self):
        self.assertEqual("odd", factor_group(36))

    def test_3(self):
        self.assertEqual("even", factor_group(7))

    def test_4(self):
        self.assertEqual("odd", factor_group(1))

    def test_5(self):
        self.assertEqual("even", factor_group(19))

    def test_6(self):
        self.assertEqual("even", factor_group(27))

    def test_7(self):
        self.assertEqual("odd", factor_group(100))

    def test_8(self):
        self.assertEqual("even", factor_group(18))

    def test_9(self):
        self.assertEqual("odd", factor_group(16))


if __name__ == "__main__":
    unittest.main()