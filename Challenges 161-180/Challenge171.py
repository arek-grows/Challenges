from __future__ import annotations
import unittest


def sum_missing_numbers(numbers: list[int]) -> int:
    adding_list = []
    for x in range(min(numbers), max(numbers) + 1):
        if x not in numbers:
            adding_list.append(x)
    return sum(adding_list)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_missing_numbers([1, 2, 3, 4, 5]), 0)

    def test_2(self):
        self.assertEqual(sum_missing_numbers([4, 3, 8, 1, 2]), 18)

    def test_3(self):
        self.assertEqual(sum_missing_numbers([17, 16, 15, 10, 11, 12]), 27)

    def test_4(self):
        self.assertEqual(sum_missing_numbers([-1, -4, -3, -2, -6, -8]), -12)


if __name__ == "__main__":
    unittest.main()