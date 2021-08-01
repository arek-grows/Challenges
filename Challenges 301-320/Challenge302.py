from __future__ import annotations
import unittest


def get_identity_matrix(dimension: int) -> list[list[int]]:
    size = abs(dimension)
    end_matrix = []
    [end_matrix.append([0] * size) for x in range(size)]
    if dimension < 0:
        for x, y in zip(range(size), range(-1, dimension - 1, -1)):
            end_matrix[x][y] = 1
    else:
        for i in range(size):
            end_matrix[i][i] = 1
    return end_matrix  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(get_identity_matrix(1), [[1]])

    def test_2(self):
        self.assertListEqual(get_identity_matrix(2), [[1, 0], [0, 1]])

    def test_3(self):
        self.assertListEqual(get_identity_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def test_4(self):
        self.assertListEqual(
            get_identity_matrix(4),
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        )

    def test_5(self):
        self.assertListEqual(
            get_identity_matrix(-6),
            [
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()