from typing import Sequence
import unittest


def marathon_distance(distances: Sequence[int]) -> bool:
    total = 0
    for d in distances:
        total += abs(d)
    return total == 25  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertFalse(marathon_distance([1, 2, 3, 4]))

    def test_2(self):
        self.assertTrue(marathon_distance([-6, 15, 4]))

    def test_3(self):
        self.assertTrue(marathon_distance([1, 9, 5, 8, 2]))

    def test_4(self):
        self.assertFalse(marathon_distance([9, 7, 6, 5]))

    def test_5(self):
        self.assertFalse(marathon_distance([4, 6, 8, 9, -4]))

    def test_6(self):
        self.assertFalse(marathon_distance([-20, 9, -10, -11]))

    def test_7(self):
        self.assertTrue(marathon_distance([-9, 15, 1]))

    def test_8(self):
        self.assertFalse(marathon_distance([]))

    def test_9(self):
        self.assertFalse(marathon_distance([]))


if __name__ == "__main__":
    unittest.main()