from typing import Union
import unittest
from math import sqrt


def iterated_sqrt(n: int) -> Union[int, str]:
    if n < 0:
        return "invalid"
    total_square_roots = 0
    while n >= 2:
        n = sqrt(n)
        total_square_roots += 1
    return total_square_roots  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(iterated_sqrt(1), 0)

    def test_2(self):
        self.assertEqual(iterated_sqrt(2), 1)

    def test_3(self):
        self.assertEqual(iterated_sqrt(7), 2)

    def test_4(self):
        self.assertEqual(iterated_sqrt(27), 3)

    def test_5(self):
        self.assertEqual(iterated_sqrt(256), 4)

    def test_6(self):
        self.assertEqual(iterated_sqrt(-1), "invalid")

    def test_7(self):
        self.assertEqual(iterated_sqrt(25), 3)

    def test_8(self):
        self.assertEqual(iterated_sqrt(59), 3)

    def test_9(self):
        self.assertEqual(iterated_sqrt(113), 3)

    def test_37(self):
        self.assertEqual(iterated_sqrt(4294967296), 6)


if __name__ == "__main__":
    unittest.main()