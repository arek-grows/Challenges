from __future__ import annotations
import unittest
from math import prod


def total_volume(*boxes: tuple[int, int, int]) -> int:
    total = 0
    for b in boxes:
        total += prod(b)
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(63, total_volume((4, 2, 4), (3, 3, 3), (1, 1, 2), (2, 1, 1)))

    def test_2(self):
        self.assertEqual(10, total_volume((2, 2, 2), (2, 1, 1)))

    def test_3(self):
        self.assertEqual(1, total_volume((1, 1, 1)))

    def test_4(self):
        self.assertEqual(68, total_volume((5, 1, 10), (1, 9, 2)))

    def test_5(self):
        self.assertEqual(14, total_volume((1, 1, 5), (3, 3, 1)))


if __name__ == "__main__":
    unittest.main()