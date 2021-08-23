from __future__ import annotations
import unittest


def balanced(lst: list[int]) -> list[int]:
    middle = int(len(lst) / 2)
    first_half = lst[:middle]
    second_half = lst[middle:]
    first_sum = sum(first_half)
    second_sum = sum(second_half)
    if first_sum == second_sum:
        return lst
    elif first_sum > second_sum:
        return first_half + first_half
    else:
        return second_half + second_half  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(balanced([1, 2, 4, 6, 3, 1]), [6, 3, 1, 6, 3, 1])

    def test_2(self):
        self.assertListEqual(
            balanced([88, 3, 27, 5, 9, 0, 13, 10]), [88, 3, 27, 5, 88, 3, 27, 5]
        )

    def test_3(self):
        self.assertListEqual(
            balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]),
            [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6],
        )

    def test_4(self):
        self.assertListEqual(balanced([0, 1, 1, 1]), [1, 1, 1, 1])

    def test_5(self):
        self.assertListEqual(balanced([100, 55]), [100, 100])


if __name__ == "__main__":
    unittest.main()