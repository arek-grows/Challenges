from __future__ import annotations
from typing import List, Union
import unittest


Card = Union[int, str]


def count(cards: list[Card]) -> int:
    total = 0
    scores = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, "J": -1, "Q": -1, "K": -1, "A": -1}
    for c in cards:
        total += scores[c]
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, count([5, 9, 10, 3, 'J', 'A', 4, 8, 5]))

    def test_2(self):
        self.assertEqual(-6, count(['A', 'A', 'K', 'Q', 'Q', 'J']))

    def test_3(self):
        self.assertEqual(5, count(['A', 5, 5, 2, 6, 2, 3, 8, 9, 7]))

    def test_4(self):
        self.assertEqual(8, count([2, 2, 2, 2, 2, 2, 2, 2]))

    def test_5(self):
        self.assertEqual(0, count([]))

    def test_6(self):
        self.assertEqual(-7, count(['A', 'A', 'A', 'A', 'A', 'A', 'A']))

    def test_7(self):
        self.assertEqual(0, count(['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]))


if __name__ == "__main__":
    unittest.main()