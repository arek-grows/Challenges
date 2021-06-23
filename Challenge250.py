from __future__ import annotations
import unittest


def count_boomerangs(boomerangs: list) -> int:
    total = 0
    for i in range(0, len(boomerangs) - 2):
        if (boomerangs[i] == boomerangs[i + 2]) and (boomerangs[i] != boomerangs[i + 1]):
            total += 1
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_boomerangs([9, 5, 9, 5, 1, 1, 1]), 2)

    def test_2(self):
        self.assertEqual(count_boomerangs([5, 6, 6, 7, 6, 3, 9]), 1)

    def test_3(self):
        self.assertEqual(count_boomerangs([4, 4, 4, 9, 9, 9, 9]), 0)

    def test_4(self):
        self.assertEqual(count_boomerangs([5, 9, 5, 9, 5]), 3)

    def test_5(self):
        self.assertEqual(count_boomerangs([4, 4, 4, 8, 4, 8, 4]), 3)

    def test_6(self):
        self.assertEqual(count_boomerangs([2, 2, 2, 2, 2, 2, 3]), 0)

    def test_7(self):
        self.assertEqual(count_boomerangs([2, 2, 2, 2, 3, 2, 3]), 2)

    def test_8(self):
        self.assertEqual(count_boomerangs([1, 2, 1, 1, 1, 2, 1]), 2)

    def test_9(self):
        self.assertEqual(count_boomerangs([5, 1, 1, 1, 1, 4, 1]), 1)

    def test_10(self):
        self.assertEqual(count_boomerangs([3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2]), 3)

    def test_11(self):
        self.assertEqual(count_boomerangs([1, 7, 1, 7, 1, 7, 1]), 5)

    def test_12(self):
        self.assertEqual(count_boomerangs([5, 5, 5]), 0)


if __name__ == "__main__":
    unittest.main()
