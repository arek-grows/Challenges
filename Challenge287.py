from __future__ import annotations
import unittest


def ones_infection(string: list[list[int]]) -> list[list[int]]:
    end_matrix = [[0] * len(string[0])] * len(string)
    # rows
    for x, s in enumerate(string):
        if 1 in s:
            end_matrix[x] = [1] * len(s)
    # columns
    for r in range(len(string[0])):  # column indexes
        for c in range(len(string)):  # row indexes

            if string[c][r] == 1:  # if 1 in the column, reloop through the column to change every item to 1
                for x in range(len(string)):
                    end_matrix[x][r] = 1
                break
    return end_matrix  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(
            ones_infection([[0, 0, 1], [0, 0, 0], [0, 0, 0]]),
            [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
        )

    def test_2(self):
        self.assertListEqual(
            ones_infection([[1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]),
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]],
        )

    def test_3(self):
        self.assertListEqual(
            ones_infection([[0, 1, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0]]),
            [[1, 1, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1]],
        )

    def test_4(self):
        self.assertListEqual(
            ones_infection([[0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0]]),
            [[1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1]],
        )

    def test_5(self):
        self.assertListEqual(
            ones_infection([[1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            [[1, 1, 1, 1], [1, 0, 1, 0], [1, 0, 1, 0]],
        )

    def test_6(self):
        self.assertListEqual(
            ones_infection([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]),
            [[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]],
        )


if __name__ == "__main__":
    unittest.main()