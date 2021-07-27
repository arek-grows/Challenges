from __future__ import annotations
import unittest
import math


def line_length(point_a: tuple[int, int], point_b: tuple[int, int]) -> float:
    distance = math.sqrt(((point_b[0] - point_a[0]) ** 2) + ((point_b[1] - point_a[1]) ** 2))
    return round(distance, 2)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(line_length((15, 7), (22, 11)), 8.06)

    def test_2(self):
        self.assertEqual(line_length((0, 0), (0, 0)), 0)

    def test_3(self):
        self.assertEqual(line_length((0, 0), (1, 1)), 1.41)

    def test_4(self):
        self.assertEqual(line_length((30, 10), (13, -5)), 22.67)


if __name__ == "__main__":
    unittest.main()
