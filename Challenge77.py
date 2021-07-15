from typing import List
import unittest


def yahtzee_upper(dice: List[int]) -> int:
    scores = []
    for x in range(1, 7):
        scores.append(x * dice.count(x))
    return max(scores)  # Put your code here!!!


class TestYahtzeeUpper(unittest.TestCase):
    def test_1(self):
        self.assertEqual(10, yahtzee_upper([2, 3, 5, 5, 6]))

    def test_2(self):
        self.assertEqual(4, yahtzee_upper([1, 1, 1, 1, 3]))

    def test_3(self):
        self.assertEqual(6, yahtzee_upper([1, 1, 1, 3, 3]))

    def test_4(self):
        self.assertEqual(5, yahtzee_upper([1, 2, 3, 4, 5]))

    def test_5(self):
        self.assertEqual(30, yahtzee_upper([6, 6, 6, 6, 6]))


if __name__ == "__main__":
    unittest.main()