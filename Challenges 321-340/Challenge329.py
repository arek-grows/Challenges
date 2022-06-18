from __future__ import annotations
import unittest


def win_round(players_hand: list[int], opponents_hand: list[int]) -> bool:
    players_hand.sort()
    opponents_hand.sort()
    if players_hand[-1] > opponents_hand[-1]:
        return True
    elif players_hand[-2] > opponents_hand[-2]:
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]))

    def test_2(self):
        self.assertFalse(win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))

    def test_3(self):
        self.assertFalse(win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]))

    def test_4(self):
        self.assertTrue(win_round([3, 2, 8, 9, 4], [0, 7, 9, 3, 1]))

    def test_5(self):
        self.assertTrue(win_round([1, 4, 9, 2, 1], [3, 7, 7, 8, 7]))

    def test_6(self):
        self.assertTrue(win_round([6, 5, 5, 8, 5], [6, 2, 5, 2, 5]))

    def test_7(self):
        self.assertFalse(win_round([5, 3, 5, 9, 2], [5, 9, 2, 8, 0]))

    def test_8(self):
        self.assertFalse(win_round([3, 2, 0, 3, 5], [7, 5, 8, 6, 2]))

    def test_9(self):
        self.assertTrue(win_round([4, 1, 0, 2, 9], [3, 5, 5, 2, 8]))

    def test_10(self):
        self.assertTrue(win_round([9, 8, 7, 3, 4], [5, 3, 4, 7, 9]))


if __name__ == "__main__":
    unittest.main()