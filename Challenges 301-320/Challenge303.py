from __future__ import annotations
import unittest


def get_list_of_sums(lst: list[int]) -> list[int]:
    totals_list = list()
    for idx in range(len(lst)):
        total = 0
        for ii, item in enumerate(lst):
            if idx == ii:
                continue
            total += item
        totals_list.append(total)
    return totals_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(get_list_of_sums([1, 2]), [2, 1])

    def test_2(self):
        self.assertListEqual(get_list_of_sums([1, 2, 3]), [5, 4, 3])

    def test_3(self):
        self.assertListEqual(get_list_of_sums([1, 2, 3, 4, 5]), [14, 13, 12, 11, 10])

    def test_4(self):
        self.assertListEqual(
            get_list_of_sums([10, 20, 30, 40, 50, 60]), [200, 190, 180, 170, 160, 150]
        )


if __name__ == "__main__":
    unittest.main()