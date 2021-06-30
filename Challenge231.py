from __future__ import annotations
from typing import TypeVar
import unittest


T = TypeVar("T")


def advanced_sort(lst: list[T]) -> list[list[T]]:
    accounted_for = []
    end_list = []
    for i in lst:
        if i not in accounted_for:
            end_list.append([i] * lst.count(i))
            accounted_for.append(i)
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(advanced_sort([1, 2, 1, 2]), [[1, 1], [2, 2]])

    def test_2(self):
        self.assertEqual(advanced_sort([2, 1, 2, 1]), [[2, 2], [1, 1]])

    def test_3(self):
        self.assertEqual(advanced_sort([3, 2, 1, 3, 2, 1]), [[3, 3], [2, 2], [1, 1]])

    def test_4(self):
        self.assertEqual(advanced_sort([5, 5, 4, 3, 4, 4]), [[5, 5], [4, 4, 4], [3]])

    def test_5(self):
        self.assertEqual(
            advanced_sort([80, 80, 4, 60, 60, 3]), [[80, 80], [4], [60, 60], [3]]
        )

    def test_6(self):
        self.assertEqual(
            advanced_sort(["c", "c", "b", "c", "b", 1, 1]),
            [["c", "c", "c"], ["b", "b"], [1, 1]],
        )

    def test_7(self):
        self.assertEqual(
            advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]),
            [[1234, 1234], [1235, 1235, 1235], [1236]],
        )

    def test_8(self):
        self.assertEqual(
            advanced_sort(["1234", "1235", "1234", "1235", "1236", "1235"]),
            [["1234", "1234"], ["1235", "1235", "1235"], ["1236"]],
        )


if __name__ == "__main__":
    unittest.main()