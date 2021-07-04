import unittest
from typing import List


def is_legitimate(pool: List[List[int]]) -> bool:
    if sum(pool[0]) != 0 or sum(pool[-1]) != 0:
        return False
    for n in pool[1:len(pool) - 2]:
        if n[0] != 0 or n[-1] != 0:
            return False
    return True  # Replace with your code!


class TestSwimmingPools(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]
            ), True)

    def test_2(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0]
                ]
            ), False)

    def test_3(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ]
            ), True)

    def test_4(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ]
            ), False)

    def test_5(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]
            ), True)

    def test_6(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]
            ), True)

    def test_7(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]
                ]
            ), True)

    def test_8(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1]
                ]
            ), False)

    def test_9(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]
                ]
            ), False)

    def test_10(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 0, 0]
                ]
            ), True)

    def test_11(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 1],
                    [0, 1, 0],
                    [0, 0, 0]
                ]
            ), False)

    def test_12(self):
        self.assertEqual(
            is_legitimate(
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0],
                    [0, 0, 0]
                ]
            ), False)


if __name__ == "__main__":
    unittest.main()