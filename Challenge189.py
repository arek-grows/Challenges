# Challenge 189 - All Occurrences of an Element in a List
#
# Create a function that returns the indices of all occurrences of an item in the list.
# Examples
#
# get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
#
# get_indices([1, 5, 5, 2, 7], 7) ➞ [4]
#
# get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]
#
# get_indices([1, 5, 5, 2, 7], 8) ➞ []
#
# Notes
#
#     If an element does not exist in a list, return an empty list.
#     Lists are zero-indexed.
#     Values in the list will be value-types (don't need to worry about nested lists).


from __future__ import annotations
from typing import Any
import unittest


def get_indices(sequence: list[Any], search_for: Any) -> list[int]:
    indexes = []
    i = 0
    for i in sequence:
        if i == search_for:
            indexes.append(i)
        i += 1
    return indexes  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_indices(["a", "a", "b", "a", "b", "a"], "a"), [0, 1, 3, 5])

    def test_2(self):
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 7), [4])

    def test_3(self):
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 5), [1, 2])

    def test_4(self):
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 8), [])

    def test_5(self):
        self.assertEqual(get_indices([8, 8, 8, 8, 8], 8), [0, 1, 2, 3, 4])

    def test_6(self):
        self.assertEqual(get_indices([8, 8, 7, 8, 8], 8), [0, 1, 3, 4])

    def test_7(self):
        self.assertEqual(get_indices([True, False, True, False], True), [0, 2])

    def test_8(self):
        self.assertEqual(get_indices([True, False, True, False], False), [1, 3])


if __name__ == "__main__":
    unittest.main()