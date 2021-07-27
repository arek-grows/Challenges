from typing import Sequence
import unittest


def war_of_numbers(numbers: Sequence[int]) -> int:
    even_total = 0
    odd_total = 0
    for n in numbers:
        if n % 2 == 0:
            even_total += n
        else:
            odd_total += n
    return abs(even_total - odd_total)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(168, war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))

    def test_2(self):
        self.assertEqual(793, war_of_numbers([654, 7, 23, 3, 78, 4, 56, 34]))

    def test_3(self):
        self.assertEqual(5, war_of_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_4(self):
        self.assertEqual(228, war_of_numbers([97, 83, 209, 141, 134, 298, 110, 207, 229, 275, 115, 64, 244, 278]))

    def test_5(self):
        self.assertEqual(83, war_of_numbers([332, 92, 35, 315, 109, 168, 320, 230, 63, 323, 16, 204, 105, 17, 226, 157, 245, 44, 223, 136, 93]))

    def test_6(self):
        self.assertEqual(846, war_of_numbers([322, 89, 36, 310, 297, 157, 251, 55, 264, 244, 200, 304, 25, 308, 311, 269, 303, 257, 6, 311, 307, 310, 50, 46, 54, 237, 59, 105, 267]))

    def test_7(self):
        self.assertEqual(0, war_of_numbers([50, 100, 149, 1, 200, 199, 3, 2]))


if __name__ == "__main__":
    unittest.main()