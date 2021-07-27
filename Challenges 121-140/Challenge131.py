from typing import Any, List
import unittest


def sort(lst: List[Any], mode: str) -> List[Any]:
    if mode == 'Asc':
        lst.sort()
        return lst
    elif mode == 'Des':
        lst.sort()
        return lst[::-1]
    return lst  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2, 3, 4], sort([4, 3, 2, 1], "Asc"))

    def test_2(self):
        self.assertEqual([66, 11, 8, 7], sort([7, 8, 11, 66], "Des"))

    def test_3(self):
        self.assertEqual([1, 2, 3, 4], sort([1, 2, 3, 4], "None"))

    def test_4(self):
        self.assertEqual([0, 0, 1, 1], sort([1, 0, 1, 0], "Asc"))

    def test_5(self):
        self.assertEqual([2, 2, 2, 2, 2, 2, 1], sort([1, 2, 2, 2, 2, 2, 2], "Des"))

    def test_6(self):
        self.assertEqual([7, 9, 11, 16, 19, 43, 111], sort([9, 7, 43, 11, 16, 111, 19], "Asc"))


if __name__ == "__main__":
    unittest.main()