from typing import Sequence
import unittest


Matrix = Sequence[Sequence[int]]


def trace(matrix: Matrix) -> int:
    total = 0
    for x in range(len(matrix)):
        total += matrix[x][x]
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, trace([[1, 4], [4, 1]]))

    def test_2(self):
        self.assertEqual(15, trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_3(self):
        self.assertEqual(12345, trace([[12345]],))

    def test_4(self):
        self.assertEqual(10, trace([[1, 0, 1, 0], [0, 2, 0, 2], [3, 0, 3, 0], [0, 4, 0, 4]]))

    def test_5(self):
        self.assertEqual(0, trace([[0, 1, 0, 1], [2, 0, 2, 0], [0, 3, 0, 3], [4, 0, 4, 0]]))

    def test_6(self):
        self.assertEqual(32, trace([[1, 8, 9, 16], [2, 7, 10, 15], [3, 6, 11, 14], [4, 5, 12, 13]]))


if __name__ == "__main__":
    unittest.main()