from __future__ import annotations
from typing import Union
import unittest


def temp_conversion(celsius: float) -> Union[tuple[float, float], str]:
    fahrenheit = round(celsius * 9 / 5 + 32, 2)
    kelvin = round(celsius + 273.15, 2)
    if kelvin < 0:
        return "Invalid"
    return fahrenheit, kelvin  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual((32, 273.15), temp_conversion(0))

    def test_2(self):
        self.assertEqual((212, 373.15), temp_conversion(100))

    def test_3(self):
        self.assertEqual((109.04, 315.95), temp_conversion(42.8))

    def test_4(self):
        self.assertEqual((572.72, 573.55), temp_conversion(300.4))

    def test_5(self):
        self.assertEqual((12.74, 262.45), temp_conversion(-10.7))

    def test_6(self):
        self.assertEqual((-459.63, 0.02), temp_conversion(-273.13))

    def test_7(self):
        self.assertEqual("Invalid", temp_conversion(-273.16))


if __name__ == "__main__":
    unittest.main()