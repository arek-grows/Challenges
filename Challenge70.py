import unittest
from typing import List


def rolls(dice: List[int]) -> int:
    total = 0
    one = False
    six = False
    for d in dice:
        if one:
            one = False
        elif six:
            total += d * 2
            six = False
        else:
            total += d

        if d == 1:
            one = True
        elif d == 6:
            six = True
    return total  # Put your code here!!!


class TestRolls(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, rolls([1, 2, 3]))

    def test_2(self):
        self.assertEqual(17, rolls([2, 6, 2, 5]))

    def test_3(self):
        self.assertEqual(8, rolls([6, 1, 1]))

    def test_4(self):
        self.assertEqual(8, rolls([5, 1, 6, 1, 6]))

    def test_5(self):
        self.assertEqual(1, rolls([1, 1, 1]))

    def test_6(self):
        self.assertEqual(2, rolls([1, 1, 3, 1, 1]))

    def test_7(self):
        self.assertEqual(1, rolls([1, 1, 1, 1, 1]))

    def test_8(self):
        self.assertEqual(30, rolls([6, 6, 6]))


if __name__ == "__main__":
    unittest.main()