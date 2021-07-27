from typing import Sequence
import unittest


def probability(numbers: Sequence[int], n: int) -> float:
    favorables = 0
    for x in numbers:
        if x >= n:
            favorables += 1
    return round(favorables / len(numbers) * 100, 1)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(50.0, probability([14, 19, 2, 6], 12))

    def test_2(self):
        self.assertEqual(33.3, probability([11, 10, 9, 18, 16, 18, 4, 3, 5], 13))

    def test_3(self):
        self.assertEqual(0.0, probability([2, 13, 1, 11, 6, 9, 11, 14, 3], 15))

    def test_4(self):
        self.assertEqual(62.5, probability([11, 6, 17, 2, 1, 16, 20, 15], 7))

    def test_5(self):
        self.assertEqual(100.0, probability([12, 15, 12, 8, 20, 16, 1], 1))

    def test_6(self):
        self.assertEqual(83.3, probability([15, 8, 12, 1, 11, 4], 4))

    def test_7(self):
        self.assertEqual(71.4, probability([14, 11, 16, 3, 13, 14, 3], 8))

    def test_8(self):
        self.assertEqual(0.0, probability([1, 4, 18, 19, 15, 3, 3, 11], 23))

    def test_9(self):
        self.assertEqual(100.0, probability([9, 8, 17, 13, 17], 8))

    def test_10(self):
        self.assertEqual(70.0, probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))


if __name__ == "__main__":
    unittest.main()