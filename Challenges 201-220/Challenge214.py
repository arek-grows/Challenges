# Challenge 214 - Find the Fulcrum
#
# A fulcrum of a list is an integer such that all elements to the left of it and all elements to the right of it sum to the same value. Write a function that finds the fulcrum of a list.
#
# To illustrate:
#
# find_fulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
# # Since [3, 1, 5] and [4, 6, -1] both sum to 9
#
# Examples
#
# find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4
#
# find_fulcrum([9, 1, 9]) ➞ 1
#
# find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0
#
# find_fulcrum([8, 8, 8, 8]) ➞ -1
#
# Notes
#
#     If the fulcrum does not exist, return -1.
#     Exclude the leftmost and rightmost elements when computing the fulcrum (it doesn't make sense to sum zero values).
#     If a list has multiple fulcrums, return the one that occurs first.


from __future__ import annotations
import unittest


def find_fulcrum(numbers: list[int]) -> int:
    for i in range(1, len(numbers)):
        sum1 = 0
        sum2 = 0
        for number in numbers[:i]:
            sum1 += number
        for number in numbers[i+1:]:
            sum2 += number
        if sum1 == sum2:
            return numbers[i]
    return -1  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]), 4)

    def test_2(self):
        self.assertEqual(find_fulcrum([9, 1, 9]), 1)

    def test_3(self):
        self.assertEqual(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]), 0)

    def test_4(self):
        self.assertEqual(find_fulcrum([8, 8, 8, 8]), -1)

    def test_5(self):
        self.assertEqual(find_fulcrum([9, 3, 4, 8, 1]), -1)

    def test_6(self):
        self.assertEqual(find_fulcrum([1, -1, 10, 5, -4, -1]), 10)


if __name__ == "__main__":
    unittest.main()
