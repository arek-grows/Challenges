from typing import Any
import unittest


def move_zeros(lst: list) -> list:
    zero_indexes = []
    for x, i in enumerate(lst):
        if (type(i) is int or type(i) is float) and i == 0:
            zero_indexes.append(x)
    lst += [0] * len(zero_indexes)
    remover = 0
    for z in zero_indexes:
        lst.pop(z-remover)
        remover += 1
    return lst  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

    def test_2(self):
        self.assertEqual(
            move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    def test_3(self):
        self.assertEqual(
            move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    def test_4(self):
        self.assertEqual(
            move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, 0, 0, 9]),
            ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    def test_5(self):
        self.assertEqual(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])

    def test_6(self):
        self.assertEqual(move_zeros(["a", "b"]), ["a", "b"])

    def test_7(self):
        self.assertEqual(move_zeros(["a"]), ["a"])

    def test_8(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])

    def test_9(self):
        self.assertEqual(move_zeros([0]), [0])

    def test_10(self):
        self.assertEqual(move_zeros([False]), [False])

    def test_11(self):
        self.assertEqual(move_zeros([]), [])


if __name__ == "__main__":
    unittest.main()