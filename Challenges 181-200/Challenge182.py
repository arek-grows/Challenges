from __future__ import annotations
import unittest


def sum_fractions(*fractions) -> int:
    total = 0
    for fraction in fractions:
        total += fraction[0] / fraction[1]
    return int(total)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_fractions((36, 4), (22, 60)), 9)

    def test_2(self):
        self.assertEqual(sum_fractions((-11, 12), (18, 13), (4, 5)), 1)

    def test_3(self):
        self.assertEqual(sum_fractions((11, 12), (18, 13), (4, 5)), 3)

    def test_4(self):
        self.assertEqual(sum_fractions((18, 13), (4, 5)), 2)

    def test_5(self):
        self.assertEqual(sum_fractions((41, 14), (10, 91)), 3)

    def test_6(self):
        self.assertEqual(sum_fractions((11, 2), (3, 4), (5, 4), (21, 11), (12, 6)), 11)


if __name__ == "__main__":
    unittest.main()