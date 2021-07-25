from __future__ import annotations
import unittest


def pos_neg_sort(numbers: list[int]) -> list[int]:
    positives = [x for x in numbers if x >= 0]
    positives.sort()
    p_idx = 0
    for x, n in enumerate(numbers):
        if n >= 0:
            numbers[x] = positives[p_idx]
            p_idx += 1
    return numbers  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(
            pos_neg_sort([6, 3, -2, 5, -8, 2, -2]), [2, 3, -2, 5, -8, 6, -2]
        )

    def test_2(self):
        self.assertListEqual(
            pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]), [1, 2, 3, -1, 4, 5, -1, 6]
        )

    def test_3(self):
        self.assertListEqual(
            pos_neg_sort([-5, -5, -5, -5, 7, -5]), [-5, -5, -5, -5, 7, -5]
        )

    def test_4(self):
        self.assertListEqual(
            pos_neg_sort([-5, -5, -5, -5, -4, -5]), [-5, -5, -5, -5, -4, -5]
        )

    def test_5(self):
        self.assertListEqual(
            pos_neg_sort([-5, 4, -8, 3, -1, 2, 1, -7]), [-5, 1, -8, 2, -1, 3, 4, -7]
        )

    def test_6(self):
        self.assertListEqual(pos_neg_sort([-5, 4, 3]), [-5, 3, 4])

    def test_7(self):
        self.assertListEqual(pos_neg_sort([]), [])


if __name__ == "__main__":
    unittest.main()