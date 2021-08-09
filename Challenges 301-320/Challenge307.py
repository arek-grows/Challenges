from __future__ import annotations
import unittest


def consecutive_combo(lst_a: list[int], lst_b: list[int]) -> bool:
    end_list = lst_a + lst_b
    end_list.sort()
    for ii, xx in enumerate(end_list[1:]):
        if end_list[ii] + 1 == xx:
            continue
        return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(consecutive_combo([1, 4, 5, 7], [2, 3, 6]))

    def test_2(self):
        self.assertFalse(consecutive_combo([1, 4, 5, 6], [2, 7, 8, 9]))

    def test_3(self):
        self.assertFalse(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))

    def test_4(self):
        self.assertTrue(consecutive_combo([7, 5, 4, 1], [2, 3, 6, 8]))

    def test_5(self):
        self.assertTrue(
            consecutive_combo([33, 34, 40], [39, 38, 37, 36, 35, 32, 31, 30])
        )

    def test_6(self):
        self.assertFalse(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))

    def test_7(self):
        self.assertTrue(consecutive_combo([44, 46], [45]))

    def test_8(self):
        self.assertTrue(consecutive_combo([4, 3, 1], [2, 5]))

    def test_9(self):
        self.assertTrue(consecutive_combo([4, 3, 1], [2, 5, 7, 6]))

    def test_10(self):
        self.assertFalse(consecutive_combo([4, 3, 1], [7, 6, 5]))

    def test_11(self):
        self.assertFalse(consecutive_combo([4, 3, 1], [0, 7, 6, 5]))

    def test_12(self):
        self.assertTrue(consecutive_combo([44, 46], [45]))


if __name__ == "__main__":
    unittest.main()