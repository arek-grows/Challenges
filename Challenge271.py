from __future__ import annotations
import unittest


def total_volume(*boxes: list[int]) -> int:
    total = 0
    for box in boxes:
        total += box[0] * box[1] * box[2]
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]), 63)

    def test_2(self):
        self.assertEqual(total_volume([2, 2, 2], [2, 1, 1]), 10)

    def test_3(self):
        self.assertEqual(total_volume([1, 1, 1]), 1)

    def test_4(self):
        self.assertEqual(total_volume([5, 1, 10], [1, 9, 2]), 68)

    def test_5(self):
        self.assertEqual(total_volume([1, 1, 5], [3, 3, 1]), 14)


if __name__ == "__main__":
    unittest.main()