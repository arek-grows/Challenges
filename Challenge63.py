import unittest
from typing import List


def is_mini_sudoku(square: List[List[int]]) -> bool:
    mini_list = []
    for s in square:
        mini_list += s
    mini_list.sort()
    return mini_list == [x for x in range(1, 10)]  # Put your code here!!!


class TestMiniSudoku(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_mini_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))

    def test_2(self):
        self.assertFalse(is_mini_sudoku([[1, 1, 3], [6, 5, 4], [8, 7, 9]]))

    def test_3(self):
        self.assertFalse(is_mini_sudoku([[0, 1, 2], [6, 4, 5], [9, 8, 7]]))

    def test_4(self):
        self.assertTrue(is_mini_sudoku([[8, 9, 2], [5, 6, 1], [3, 7, 4]]))

    def test_5(self):
        self.assertFalse(is_mini_sudoku([[2, 3, 4], [6, 7, 7], [8, 9, 1]]))

    def test_6(self):
        self.assertTrue(is_mini_sudoku([[6, 5, 9], [4, 3, 8], [2, 1, 7]]))

    def test_7(self):
        self.assertTrue(is_mini_sudoku([[4, 3, 5], [8, 1, 2], [9, 6, 7]]))

    def test_8(self):
        self.assertFalse(is_mini_sudoku([[4, 3, 5], [8, 6, 2], [9, 6, 7]]))


if __name__ == "__main__":
    unittest.main()