from __future__ import annotations
import unittest


def largest_gap(numbers: list[int]) -> int:
    lgest_gap = 0
    numbers.sort()
    for ii in range(0, len(numbers) - 1):
        gap = numbers[ii + 1] - numbers[ii]
        if gap > lgest_gap:
            lgest_gap = gap
    return lgest_gap  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]), 11)

    def test_2(self):
        self.assertEqual(largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]), 4)

    def test_3(self):
        self.assertEqual(
            largest_gap([1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]), 2
        )

    def test_4(self):
        self.assertEqual(largest_gap([21, 28, 0, 5, 11, 6, 17, 25, 2, 19]), 6)

    def test_5(self):
        self.assertEqual(largest_gap([8, 11, 24, 2, 7, 4, 4, 25, 24, 14, 8, 0, 7]), 10)

    def test_6(self):
        self.assertEqual(
            largest_gap(
                [26, 17, 4, 25, 29, 26, 8, 30, 4, 20, 2, 7, 29, 7, 20, 30, 23, 5]
            ),
            9,
        )


if __name__ == "__main__":
    unittest.main()