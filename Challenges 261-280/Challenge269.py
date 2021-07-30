from __future__ import annotations
from typing import Any
import unittest


def get_length(lst: list[Any], total=0) -> int:
    for x in lst:
        if type(x) is not list:
            total += 1
        else:
            total = get_length(x, total)
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_length([1, [2, 3]]), 3)

    def test_2(self):
        self.assertEqual(get_length([1, [2, [3, 4]]]), 4)

    def test_3(self):
        self.assertEqual(get_length([1, [2, [3, [4, [5, 6]]]]]), 6)

    def test_4(self):
        self.assertEqual(get_length([1, 7, 8]), 3)

    def test_5(self):
        self.assertEqual(get_length([2]), 1)

    def test_6(self):
        self.assertEqual(get_length([2, [3], 4, [7]]), 4)

    def test_7(self):
        self.assertEqual(get_length([2, [3, [5, 7]], 4, [7]]), 6)

    def test_8(self):
        self.assertEqual(get_length([2, [3, [4, [5]]], [9]]), 5)

    def test_9(self):
        self.assertEqual(get_length([]), 0)


if __name__ == "__main__":
    unittest.main()