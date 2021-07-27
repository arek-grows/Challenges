from typing import Union
import unittest


def valid_division(equation: str) -> Union[str, bool]:
    equation = equation.split('/')
    numerator = int(equation[0])
    denominator = int(equation[1])
    try:
        if numerator / denominator % 1 == 0:
            return True
        else:
            return False
    except ZeroDivisionError:
        return "invalid"


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(valid_division("6/3"))

    def test_2(self):
        self.assertFalse(valid_division("30/25"))

    def test_3(self):
        self.assertTrue(valid_division("0/3"))

    def test_4(self):
        self.assertFalse(valid_division("13/12"))

    def test_5(self):
        self.assertTrue(valid_division("329/329"))

    def test_6(self):
        self.assertTrue(valid_division("20/5"))

    def test_7(self):
        self.assertEqual(valid_division("0/0"), "invalid")

    def test_8(self):
        self.assertEqual(valid_division("10/0"), "invalid")


if __name__ == "__main__":
    unittest.main()