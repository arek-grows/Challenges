from __future__ import annotations
import unittest


def count_true(boomerangs: list) -> int:
    return boomerangs.count(True)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_true([True, False, False, True, False]), 2)

    def test_2(self):
        self.assertEqual(count_true([False, False, False, False]), 0)

    def test_3(self):
        self.assertEqual(count_true([]), 0)

    def test_4(self):
        self.assertEqual(count_true([False, False, True, True, False, False, False, True, True, True, True, False, True, True, False]), 8)

    def test_5(self):
        self.assertEqual(count_true([True, False, True, True, False, False, False, False, False]), 3)

    def test_6(self):
        self.assertEqual(count_true([False, True, True, False, True, True, False, True, False, True, False, True, False, True, False]), 8)

    def test_7(self):
        self.assertEqual(count_true([True, False, True, True, True, False, True, True, False, False]), 6)

    def test_8(self):
        self.assertEqual(count_true([False, False, False, False, True, False, True, False, True, False, False]), 3)

    def test_9(self):
        self.assertEqual(count_true([True, False, False, False, True, False, False, True, False, False, False]), 3)

    def test_10(self):
        self.assertEqual(count_true([True, True, False, True, False, False, False, False, True, False]), 4)

    def test_11(self):
        self.assertEqual(count_true([True, False, True, True, False, True, True, True, True, False, True, False, True, False]), 9)

    def test_12(self):
        self.assertEqual(count_true([True, False, True, True, True, True, False, True, True, False, True, False, False, False, False]), 8)

    def test_13(self):
        self.assertEqual(count_true([True, True, False, False, False, False, True, False, True, True, False, True]), 6)


if __name__ == "__main__":
    unittest.main()