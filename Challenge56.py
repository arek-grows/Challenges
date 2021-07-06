import unittest
from typing import List


def w(field: List[List[int]]) -> int:
    total = 0
    for f in field:
        total += sum(f)
    return total  # Put your code here!


class TestW(unittest.TestCase):
    def test_1(self):
        self.assertEqual(8, w([[1, 1, 0], [1, 1, 1], [1, 1, 1]]))

    def test_2(self):
        self.assertEqual(12, w([[2, 2, 2], [1, 1, 1], [1, 1, 1]]))

    def test_3(self):
        self.assertEqual(0, w([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_4(self):
        self.assertEqual(9, w([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

    def test_5(self):
        self.assertEqual(16, w([[5, 1, 2], [1, 1, 1], [1, 2, 2]]))


if __name__ == "__main__":
    unittest.main()