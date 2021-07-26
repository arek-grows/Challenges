from __future__ import annotations
import unittest


def replace_next_largest(numbers: list[int]) -> list[int]:
    in_order = []
    # remove duplicates
    [in_order.append(x) for x in numbers if x not in in_order]
    # sort the list then add -1 to the end
    in_order.sort()
    in_order.append(-1)
    end_list = []
    for n in numbers:
        # in_order[in_order.index(n) + 1] == the next highest number, so append that to end_list
        end_list.append(in_order[in_order.index(n) + 1])
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        # not_in_order == [5, 7, 3, 2, 8]; in_order ==
        self.assertListEqual(replace_next_largest([5, 7, 3, 2, 8]), [7, 8, 5, 3, -1])

    def test_2(self):
        self.assertListEqual(
            replace_next_largest([4, 1, 6, -7, -8, 2]), [6, 2, -1, 1, -7, 4]
        )

    def test_3(self):
        self.assertListEqual(replace_next_largest([2, 3, 4, 5]), [3, 4, 5, -1])

    def test_4(self):
        self.assertListEqual(
            replace_next_largest([1, 0, -1, 8, -72]), [8, 1, 0, -1, -1]
        )


if __name__ == "__main__":
    unittest.main()