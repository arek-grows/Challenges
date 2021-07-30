from __future__ import annotations
import unittest


def square_patch(n: int) -> list[list[int]]:
    end_matrix = []
    for x in range(1, n + 1):
        end_matrix.append([n] * n)
    return end_matrix  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(square_patch(3), [[3, 3, 3], [3, 3, 3], [3, 3, 3]])

    def test_2(self):
        self.assertListEqual(square_patch(2), [[2, 2], [2, 2]])

    def test_3(self):
        self.assertListEqual(
            square_patch(4), [[4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]]
        )

    def test_5(self):
        self.assertListEqual(
            square_patch(5),
            [
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
            ],
        )


if __name__ == "__main__":
    unittest.main()