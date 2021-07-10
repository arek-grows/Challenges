from typing import List
import unittest


def sum_of_evens(matrix: List[List[int]]) -> int:
    total = 0
    oned_matrix = []
    for m in matrix:
        oned_matrix += m
    for num in oned_matrix:
        if num % 2 == 0:
            total += num
    return total  # Put your code here!!!


class TestSumOfEvens(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            24, sum_of_evens([[1, 5, 1, 3], [4, 1, 2, 0], [6, 9, 7, 4], [5, 1, 2, 6]])
        )

    def test_2(self):
        self.assertEqual(
            2, sum_of_evens([[1, 0, 1], [33, 1, 2], [15, 9, 1], [5, 1, 979]])
        )

    def test_3(self):
        self.assertEqual(16, sum_of_evens([[2, 19, 5, 43], [67, 2, 0, 12]]))

    def test_4(self):
        self.assertEqual(
            0, sum_of_evens([[1, 3, 7, 9], [11, 13, 15, 17], [19, 21, 23, 25]])
        )

    def test_5(self):
        self.assertEqual(0, sum_of_evens([[], [], []]))


if __name__ == "__main__":
    unittest.main()