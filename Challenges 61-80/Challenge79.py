from typing import List, Union
import unittest


Card = Union[int, str]


def create_possible_scores(scores, card):
    if card == "A":
        new_scores = []
        for x, s in enumerate(scores):
            scores[x] += 1
            new_scores.append(s + 11)
        for score in new_scores:
            scores.append(score)
    else:
        for x, s in enumerate(scores):
            scores[x] += card
    return scores


def over_twenty_one(cards: List[Card]) -> bool:
    possible_scores = [0]
    for card in cards:
        if card in ["J", "Q", "K"]:
            possible_scores = create_possible_scores(possible_scores, 10)
        else:
            possible_scores = create_possible_scores(possible_scores, card)
    print("cards: %s | possible scores: %s" % (cards, possible_scores))
    for score in possible_scores:
        if score <= 21:
            return False
    return True  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertFalse(over_twenty_one(['A', 2, 3]))

    def test_2(self):
        self.assertFalse(over_twenty_one(['A', 'J', 'K']))

    def test_3(self):
        self.assertTrue(over_twenty_one(['A', 'J', 'K', 'Q']))

    def test_4(self):
        self.assertTrue(over_twenty_one([5, 3, 6, 6, 7, 9]))

    def test_5(self):
        self.assertFalse(over_twenty_one(['A', 'A', 'A', 8]))


if __name__ == "__main__":
    unittest.main()