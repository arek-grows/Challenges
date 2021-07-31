from __future__ import annotations
import unittest


def sum_of_two(list_a: list[int], list_b: list[int], target_value: int) -> bool:
    for a in list_a:
        for b in list_b:
            if a + b == target_value:
                return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(sum_of_two([1, 2, 3], [10, 20, 30, 40, 50], 42))

    def test_2(self):
        self.assertFalse(sum_of_two([1, 2, 3], [10, 20, 30, 40, 50], 44))

    def test_3(self):
        self.assertTrue(sum_of_two([1, 2, 3], [10, 20, 30, 40, 50], 11))

    def test_4(self):
        self.assertFalse(sum_of_two([1, 2, 3], [10, 20, 30, 40, 50], 60))

    def test_5(self):
        self.assertTrue(sum_of_two([1, 2, 3], [10, 20, 30, 40, 50], 53))

    def test_6(self):
        self.assertFalse(sum_of_two([1, 2, 3], [10, 20, 30, 40, 50], 4))


if __name__ == "__main__":
    unittest.main()