from __future__ import annotations
from typing import Union
import unittest


def last(lst: list, n: int):
    if len(lst) < n:
        return "invalid"
    end_list = []
    for x in lst[len(lst)-n:]:
        end_list.append(x)
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 0), [])

    def test_2(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 1), [5])

    def test_3(self):
        self.assertEqual(last([4, 3, 9, 9, 7, 6], 3), [9, 7, 6])

    def test_4(self):
        self.assertEqual(last([5, 1, 2], 3), [5, 1, 2])

    def test_5(self):
        self.assertEqual(last([], 1), "invalid")

    def test_6(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 7), "invalid")


if __name__ == "__main__":
    unittest.main()