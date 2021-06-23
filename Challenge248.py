from __future__ import annotations
import unittest


def has_enough_change(change: list, total: float) -> bool:
    change_total = (change[0]*0.25) + (change[1]*0.1) + (change[2]*0.05) + (change[3]*0.01)
    return change_total >= total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertFalse(has_enough_change([2, 100, 0, 0], 14.11))

    def test_2(self):
        self.assertTrue(has_enough_change([0, 0, 20, 5], 0.75))

    def test_3(self):
        self.assertTrue(has_enough_change([30, 40, 20, 5], 12.55))

    def test_4(self):
        self.assertFalse(has_enough_change([10, 0, 0, 50], 13.85))

    def test_5(self):
        self.assertFalse(has_enough_change([1, 0, 5, 219], 19.99))

    def test_6(self):
        self.assertTrue(has_enough_change([1, 0, 2555, 219], 127.75))

    def test_7(self):
        self.assertTrue(has_enough_change([1, 335, 0, 219], 35.21))


if __name__ == "__main__":
    unittest.main()