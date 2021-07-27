from typing import List, Union
import unittest


def last(lst: List[int], n: int) -> Union[List[int], str]:
    if len(lst) < n:
        return 'invalid'
    return lst[len(lst) - n:]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual([], last([1, 2, 3, 4, 5], 0))

    def test_2(self):
        self.assertEqual([5], last([1, 2, 3, 4, 5], 1))

    def test_3(self):
        self.assertEqual([9, 7, 6], last([4, 3, 9, 9, 7, 6], 3))

    def test_4(self):
        self.assertEqual([5, 1, 2], last([5, 1, 2], 3))

    def test_5(self):
        self.assertEqual("invalid", last([], 1))

    def test_6(self):
        self.assertEqual("invalid", last([1, 2, 3, 4, 5], 7))


if __name__ == "__main__":
    unittest.main()