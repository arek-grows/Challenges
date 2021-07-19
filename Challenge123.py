from typing import Any, List
import unittest


def list_builder(lists: List[List[Any]]) -> List[Any]:
    end = []
    for l in lists:
        for i in l:
            end.append(i)
    return end  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2, 3, 4], list_builder([[1, 2], [3, 4]]))

    def test_2(self):
        self.assertEqual(['a', 'b', 'c', 'd'], list_builder([['a', 'b'], ['c', 'd']]))

    def test_3(self):
        self.assertEqual([True, False, False, False], list_builder([[True, False], [False, False]]))


if __name__ == "__main__":
    unittest.main()