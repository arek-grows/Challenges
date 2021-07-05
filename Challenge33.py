import unittest
from typing import List, Tuple


def intersection_union(list_a: List[int], list_b: List[int]) -> Tuple[List[int], List[int]]:
    intersection = []
    union = []
    for a in list_a:
        if a not in union:
            union.append(a)
        if a in list_b and a not in intersection:
            intersection.append(a)
    for b in list_b:
        if b not in union:
            union.append(b)
    intersection.sort()
    union.sort()
    return intersection, union  # Put your code here!


class TestIntersectionUnion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(intersection_union([1, 2, 3, 4, 4], [4, 5, 9]), ([4], [1, 2, 3, 4, 5, 9]))

    def test_2(self):
        self.assertEqual(intersection_union([1, 2, 3], [4, 5, 6]), ([], [1, 2, 3, 4, 5, 6]))

    def test_3(self):
        self.assertEqual(intersection_union([1, 1], [1, 1, 1, 1]), ([1], [1]))

    def test_4(self):
        self.assertEqual(intersection_union([5, 5], [5, 6]), ([5], [5, 6]))

    def test_5(self):
        self.assertEqual(intersection_union([7, 8, 9, 6], [9, 7, 6, 8]), ([6, 7, 8, 9], [6, 7, 8, 9]))

    def test_6(self):
        self.assertEqual(intersection_union([4, 1, 1, 2], [1, 4, 4, 4, 4, 4, 4]), ([1, 4], [1, 2, 4]))


if __name__ == "__main__":
    unittest.main()