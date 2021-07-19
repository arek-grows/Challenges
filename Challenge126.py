from typing import List
import unittest


def factor_chain(lst: List[int]) -> bool:
    previous = lst[0]
    for nr in lst[1:]:
        if nr % previous != 0:
            return False
        previous = nr
    return True  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(factor_chain([1, 2, 4, 8, 16, 32]))

    def test_2(self):
        self.assertTrue(factor_chain([1, 1, 1, 1, 1, 1]))

    def test_3(self):
        self.assertFalse(factor_chain([2, 4, 6, 7, 12]))

    def test_4(self):
        self.assertFalse(factor_chain([10, 1]))

    def test_5(self):
        self.assertFalse(factor_chain([10, 20, 30, 40]))

    def test_6(self):
        self.assertTrue(factor_chain([10, 20, 40]))

    def test_7(self):
        self.assertTrue(factor_chain([1, 1, 1, 1, 7, 49]))


if __name__ == "__main__":
    unittest.main()