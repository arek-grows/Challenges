from __future__ import annotations
import unittest


def final(rows: int, columns: int, operations: list[str]) -> list[list[int]]:
    end_matrix = []
    for x in range(rows):
        end_matrix.append([0] * columns)
    for operation in operations:
        idx = int(operation[0])
        direction = operation[1]
        if direction == "r":
            for x in range(len(end_matrix[idx])):
                end_matrix[idx][x] += 1
        elif direction == "c":
            for x in range(len(end_matrix)):
                end_matrix[x][idx] += 1
        else:
            return "error"
    return end_matrix  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(final(2, 2, ["0r", "0r", "0r", "1c"]), [[3, 4], [0, 1]])

    def test_2(self):
        self.assertListEqual(final(2, 2, ["0c"]), [[1, 0], [1, 0]])

    def test_3(self):
        self.assertListEqual(
            final(3, 3, ["0c", "1c", "1c", "2c", "2c", "2c"]),
            [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
        )

    def test_4(self):
        self.assertListEqual(
            final(3, 3, ["2r", "2c", "1r", "0c"]), [[1, 0, 1], [2, 1, 2], [2, 1, 2]]
        )

    def test_5(self):
        self.assertListEqual(final(1, 1, []), [[0]])

    def test_6(self):
        self.assertListEqual(
            final(3, 3, ["0r", "2c", "1r", "2c", "1c", "1r", "1r"]),
            [[1, 2, 3], [3, 4, 5], [0, 1, 2]],
        )

    def test_7(self):
        self.assertListEqual(final(3, 3, []), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_8(self):
        self.assertListEqual(
            final(3, 4, ["1r", "1r", "1r", "3c", "3c", "3c"]),
            [[0, 0, 0, 3], [3, 3, 3, 6], [0, 0, 0, 3]],
        )

    def test_9(self):
        self.assertListEqual(
            final(10, 1, ["1r", "2r", "3r", "0c"]),
            [[1], [2], [2], [2], [1], [1], [1], [1], [1], [1]],
        )

    def test_10(self):
        self.assertListEqual(
            final(2, 5, ["1r", "1r", "1r", "1c", "0c", "0c", "1r", "0c", "1r", "0c"]),
            [[4, 1, 0, 0, 0], [9, 6, 5, 5, 5]],
        )


if __name__ == "__main__":
    unittest.main()