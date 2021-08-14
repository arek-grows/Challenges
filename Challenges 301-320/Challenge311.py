from __future__ import annotations
import unittest
from math import sqrt


def check_square_and_cube(numbers: list[int]) -> bool:
    sq_rt = sqrt(numbers[0])
    if sq_rt ** 3 == numbers[1]:
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(check_square_and_cube([4, 8]))

    def test_2(self):
        self.assertFalse(check_square_and_cube([5, 12]))

    def test_3(self):
        self.assertTrue(check_square_and_cube([9, 27]))

    def test_4(self):
        self.assertFalse(check_square_and_cube([25, 120]))

    def test_5(self):
        self.assertTrue(check_square_and_cube([25, 125]))

    def test_6(self):
        self.assertFalse(check_square_and_cube([36, 215]))

    def test_7(self):
        self.assertFalse(check_square_and_cube([36, 217]))

    def test_8(self):
        self.assertTrue(check_square_and_cube([144, 1728]))

    def test_9(self):
        self.assertTrue(check_square_and_cube([1, 1]))

    def test_10(self):
        self.assertTrue(check_square_and_cube([676, 17576]))


if __name__ == "__main__":
    unittest.main()