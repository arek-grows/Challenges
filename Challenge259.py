# Challenge 259 - Measure the Depth of Emptiness
#
# In this challenge you will receive an input of the form: python [[[[[[[[[[[]]]]]]]]]]] In other words,
# a list containing a list containing a list containing ... a list containing nothing.
#
# Your goal is to measure the depth of this list, where [] has a depth of 1, [[]] has depth of 2, [[[]]] has depth of
# 3, etc.
#
# Examples
#
# ```python measure_depth([]) ➞ 1
#
# measure_depth([[]]) ➞ 2
#
# measure_depth([[[]]]) ➞ 3
#
# measure_depth([[[[[[[[[[[]]]]]]]]]]]) ➞ 11 ```
#
# Notes
# •For a bonus challenge, try to find a solution without recursion.
from __future__ import annotations
import unittest


def measure_depth(lists: list[list], times) -> int:
    return 0  # Put your code here!!!`


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(measure_depth([]), 1)

    def test_2(self):
        self.assertEqual(measure_depth([[]]), 2)

    def test_3(self):
        self.assertEqual(measure_depth([[[]]]), 3)

    def test_4(self):
        self.assertEqual(measure_depth([[[[[[]]]]]]), 6)

    def test_5(self):
        self.assertEqual(measure_depth([[[[[[[[]]]]]]]]), 8)

    def test_6(self):
        self.assertEqual(measure_depth([[[[[[[[[[[[[]]]]]]]]]]]]]), 13)

    def test_7(self):
        self.assertEqual(measure_depth([[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]), 17)

    def test_8(self):
        self.assertEqual(measure_depth([[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]), 18)

    def test_9(self):
        """ Bonus test to see if your code will work without recursion. """
        import sys

        limit = sys.getrecursionlimit()
        sys.setrecursionlimit(50)
        self.assertEqual(measure_depth([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]), 50)
        sys.setrecursionlimit(limit)


if __name__ == "__main__":
    unittest.main()
