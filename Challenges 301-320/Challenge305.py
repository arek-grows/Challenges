from typing import Protocol
import unittest


class OnesThreesNinesProtocol():
    def __init__(self, n):
        self.ones = n // 1
        self.threes = n // 3
        self.nines = n // 9


def ones_threes_nines(n: int) -> OnesThreesNinesProtocol:
    return OnesThreesNinesProtocol(n)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ones_threes_nines(0).ones, 0)

    def test_2(self):
        self.assertEqual(ones_threes_nines(1).threes, 0)

    def test_3(self):
        self.assertEqual(ones_threes_nines(2).nines, 0)

    def test_4(self):
        self.assertEqual(ones_threes_nines(3).ones, 3)

    def test_5(self):
        self.assertEqual(ones_threes_nines(4).threes, 1)

    def test_6(self):
        self.assertEqual(ones_threes_nines(10).nines, 1)

    def test_7(self):
        self.assertEqual(ones_threes_nines(13).ones, 13)

    def test_8(self):
        self.assertEqual(ones_threes_nines(15).threes, 5)

    def test_9(self):
        self.assertEqual(ones_threes_nines(17).nines, 1)

    def test_10(self):
        self.assertEqual(ones_threes_nines(20).nines, 2)


if __name__ == "__main__":
    unittest.main()