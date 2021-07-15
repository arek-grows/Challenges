from typing import List, Tuple
import unittest


Interval = Tuple[int, int]


def count_overlapping(points: List[Interval], point: int) -> int:
    total = 0
    for p in points:
        if p[0] <= point <= p[1]:
            total += 1
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, count_overlapping([(1, 2), (2, 3), (3, 4)], 5))

    def test_2(self):
        self.assertEqual(2, count_overlapping([(1, 2), (5, 6), (5, 7)], 5))

    def test_3(self):
        self.assertEqual(2, count_overlapping([(1, 2), (5, 8), (6, 9)], 7))

    def test_4(self):
        self.assertEqual(5, count_overlapping([(1, 5), (2, 5), (3, 6), (4, 5), (5, 6)], 5))

    def test_5(self):
        self.assertEqual(2, count_overlapping([(1, 5), (2, 5), (3, 6), (4, 5), (5, 6)], 6))

    def test_6(self):
        self.assertEqual(2, count_overlapping([(1, 5), (2, 5), (3, 6), (4, 5), (5, 6)], 2))

    def test_7(self):
        self.assertEqual(1, count_overlapping([(1, 5), (2, 5), (3, 6), (4, 5), (5, 6)], 1))


if __name__ == "__main__":
    unittest.main()