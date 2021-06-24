from __future__ import annotations
import unittest


def sum_odd_and_even(numbers: list[int]) -> tuple[int, int]:
    even_total = 0
    odd_total = 0
    for n in numbers:
        if n % 2 == 0:
            even_total += n
        else:
            odd_total += n
    return even_total, odd_total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_odd_and_even([1, 2, 3, 4, 5, 6]), (12, 9))

    def test_2(self):
        self.assertEqual(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), (-12, -9))

    def test_3(self):
        self.assertEqual(sum_odd_and_even([0, 0]), (0, 0))

    def test_4(self):
        self.assertEqual(sum_odd_and_even([]), (0, 0))


if __name__ == "__main__":
    unittest.main()