from typing import Sequence
import unittest


def win_round(your_cards: Sequence[int], opponents_cards: Sequence[int]) -> bool:
    # the highest card sequence is the two highest numbered cards put together
    # take the highest number in both hands
    max_one = max(your_cards)
    max_two = max(opponents_cards)
    # remove the highest number so that max() can retrieve the second highest number
    your_cards.pop(your_cards.index(max_one))
    opponents_cards.pop(opponents_cards.index(max_two))
    # append highest number + second highest number
    max_one = int(str(max_one) + str(max(your_cards)))
    max_two = int(str(max_two) + str(max(opponents_cards)))
    return max_one > max_two  # return True if your hand is higher


class Test(unittest.TestCase):
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

    def test_11(self):
        self.assertTrue(win_round([3, 3, 3, 9, 9], [9, 0, 0, 6, 6]))

    def test_12(self):
        self.assertFalse(win_round([3, 2, 8, 2, 0], [8, 5, 4, 5, 7]))

    def test_13(self):
        self.assertFalse(win_round([6, 2, 6, 8, 0], [7, 6, 3, 2, 9]))

    def test_14(self):
        self.assertTrue(win_round([8, 3, 5, 3, 5], [5, 5, 4, 4, 6]))

    def test_15(self):
        self.assertFalse(win_round([4, 0, 7, 7, 7], [8, 6, 7, 6, 3]))


if __name__ == "__main__":
    unittest.main()