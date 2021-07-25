from __future__ import annotations
import unittest


def puzzle_pieces(list_a: list[int], list_b: list[int]) -> bool:
    if len(list_a) != len(list_b):
        return False
    elif len(list_a) == 1:  # no need to loop through a list with length 1
        return True
    number = list_a[0] + list_b[0]
    for a, b in zip(list_a[1:], list_b[1:]):
        if a + b != number:
            return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))

    def test_2(self):
        self.assertTrue(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))

    def test_3(self):
        self.assertTrue(puzzle_pieces([2, 1, 1], [-2, -1, -1]))

    def test_4(self):
        self.assertTrue(puzzle_pieces([2], [-2]))

    def test_5(self):
        self.assertTrue(puzzle_pieces([5, -1], [-6, 0]))

    def test_6(self):
        self.assertTrue(puzzle_pieces([0, 0, 0, 0, 0], [1, 1, 1, 1, 1]))

    def test_7(self):
        self.assertFalse(puzzle_pieces([1, 2], [-1, -1]))

    def test_8(self):
        self.assertFalse(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))

    def test_9(self):
        self.assertFalse(puzzle_pieces([9, 8, 7], [7, 8, 9, 16]))

    def test_10(self):
        self.assertFalse(puzzle_pieces([1, 1, 1], [1, 1, 2]))

    def test_11(self):
        self.assertFalse(puzzle_pieces([1, 8, 1], [1, -8, -1]))

    def test_12(self):
        self.assertFalse(puzzle_pieces([0, 0, 0, 0, 0], [1, 1, 0, 1, 1]))

    def test_13(self):
        self.assertFalse(puzzle_pieces([0, 0, 0, 0, 0], [1, 1, 1, 1]))


if __name__ == "__main__":
    unittest.main()