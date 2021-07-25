from __future__ import annotations
import unittest


def largest_even(numbers: list[int]) -> int:
    numbers.sort()
    for n in numbers[::-1]:
        if n % 2 == 0:
            return n
    return -1  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_even([3, 7, 2, 1, 7, 9, 10, 13]), 10)

    def test_2(self):
        self.assertEqual(largest_even([1]), -1)

    def test_3(self):
        self.assertEqual(largest_even([22]), 22)

    def test_4(self):
        self.assertEqual(largest_even([13, 5, 7, 9]), -1)

    def test_5(self):
        self.assertEqual(largest_even([3, 19, 18973623, 2]), 2)


if __name__ == "__main__":
    unittest.main()