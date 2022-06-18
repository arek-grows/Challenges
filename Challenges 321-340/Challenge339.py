from __future__ import annotations
import unittest


def can_be_consecutive(numbers: list[int]) -> bool:
    numbers.sort()
    previous = numbers[0]
    for nn in numbers[1:]:
        if previous + 1 != nn:
            return False
        previous = nn
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(can_be_consecutive([5, 1, 4, 3, 2]))

    def test_2(self):
        self.assertTrue(can_be_consecutive([55, 59, 58, 56, 57]))

    def test_3(self):
        self.assertTrue(can_be_consecutive([-3, -2, -1, 1, 0]))

    def test_4(self):
        self.assertFalse(can_be_consecutive([5, 1, 4, 3, 2, 8]))

    def test_5(self):
        self.assertFalse(can_be_consecutive([5, 6, 7, 8, 9, 9]))

    def test_6(self):
        self.assertFalse(can_be_consecutive([5, 3]))


if __name__ == "__main__":
    unittest.main()