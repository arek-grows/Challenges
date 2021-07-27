# Challenge 217 - Shortest Subarray Whose Sum Exceeds N
#
# Write a function that returns the length of the shortest contiguous sublist whose sum of all elements strictly exceeds n.
# Examples
#
# min_length([5, 8, 2, -1, 3, 4], 9) ➞ 2
#
# min_length([3, -1, 4, -2, -7, 2], 4) ➞ 3
# # Shortest sublist whose sum exceeds 4 is: [3, -1, 4]
#
# min_length([1, 0, 0, 0, 1], 1) ➞ 5
#
# min_length([0, 1, 1, 0], 2) ➞ -1
#
# Notes
#
#     The sublist should be composed of contiguous elements from the original list.
#     If no such sublist exists, return -1.


from __future__ import annotations
import unittest


def min_length(values: list[int], min_value: int) -> int:
    shortest_sublist_length = len(values) + 1
    impossible = shortest_sublist_length
    while len(values) > 0:
        currently_adding = []
        for x in values:
            currently_adding.append(x)
            if sum(currently_adding) > min_value and len(currently_adding) < shortest_sublist_length:
                shortest_sublist_length = len(currently_adding)
                break
        values.pop(0)
    if shortest_sublist_length == impossible:
        return -1
    return shortest_sublist_length


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min_length([5, 10, 2, -1, 3, 4], 9), 1)

    def test_2(self):
        self.assertEqual(min_length([3, -1, 4, -2, -7, 2], 4), 3)

    def test_3(self):
        self.assertEqual(min_length([-5, 3, 2, 7, 8, 9, -1, 5], 16), 2)

    def test_4(self):
        self.assertEqual(min_length([1, 0, -1, 1, 1], 1), 2)

    def test_5(self):
        self.assertEqual(min_length([1, 0, 1, 1, -1, 0, 1], 2), 4)

    def test_6(self):
        self.assertEqual(min_length([1, 0, 0, 0, 1], 1), 5)

    def test_7(self):
        self.assertEqual(min_length([1, 0, 1, 0, 1], 1), 3)

    def test_8(self):
        self.assertEqual(min_length([-1, 1, 1, 0, 1, 1], 3), 5)

    def test_9(self):
        self.assertEqual(min_length([3, -1, 4, 3, 0, 1, 2], 7), 4)

    def test_10(self):
        self.assertEqual(min_length([0, 1, 1, 0], 2), -1)

    def test_11(self):
        self.assertEqual(min_length([0, 1, 5, 2, 0], 10), -1)

    def test_12(self):
        self.assertEqual(min_length([3, -1, 4, -2, -7, 2], 6), -1)


if __name__ == "__main__":
    unittest.main()
