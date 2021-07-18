from typing import Sequence
import unittest


def decrypt(numbers: Sequence[int]) -> str:
    missing = int()
    for x in range(1, 27):
        if x not in numbers:
            missing = x
            break
    return chr(missing + 64)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            "H",
            decrypt([21, 2, 5, 25, 7, 20, 15, 3, 6, 9, 16, 19, 1, 4, 11, 22, 10, 13, 12, 18, 24, 17, 23, 14, 26])
        )

    def test_2(self):
        self.assertEqual(
            "E",
            decrypt([22, 7, 2, 15, 10, 4, 11, 25, 1, 8, 23, 12, 17, 16, 14, 13, 3, 21, 20, 6, 19, 9, 24, 18, 26])
        )

    def test_3(self):
        self.assertEqual(
            "L",
            decrypt([17, 3, 15, 6, 21, 7, 18, 5, 13, 23, 24, 16, 8, 19, 25, 2, 9, 11, 22, 10, 20, 14, 1, 4, 26])
        )

    def test_4(self):
        self.assertEqual(
            "L",
            decrypt([8, 6, 23, 4, 25, 13, 7, 19, 15, 3, 14, 5, 21, 11, 1, 2, 24, 18, 22, 16, 9, 20, 10, 17, 26])
        )

    def test_5(self):
        self.assertEqual(
            "O",
            decrypt([19, 12, 14, 21, 22, 3, 11, 20, 9, 16, 24, 17, 2, 10, 13, 18, 7, 8, 4, 5, 1, 6, 25, 23, 26])
        )


if __name__ == "__main__":
    unittest.main()