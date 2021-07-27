import unittest
from typing import Iterable


def gen_deck() -> Iterable:
    end = []
    ranks = [x for x in range(2, 11)] + ["J", "Q", "K", "A"]
    suits = ['D', 'C', 'H', 'S']
    for suit in suits:
        for rank in ranks:
            end.append((rank, suit))
    return end  # Put your code here!!!


class TestGenDeck(unittest.TestCase):
    def test_deck(self):
        self.assertEqual(
            sorted(
                gen_deck(),
                key=lambda card: (
                    ((list(range(2, 11)) + list("JQKA")).index(card[0]), card[1])
                ),
            ),
            [
                (2, "C"),
                (2, "D"),
                (2, "H"),
                (2, "S"),
                (3, "C"),
                (3, "D"),
                (3, "H"),
                (3, "S"),
                (4, "C"),
                (4, "D"),
                (4, "H"),
                (4, "S"),
                (5, "C"),
                (5, "D"),
                (5, "H"),
                (5, "S"),
                (6, "C"),
                (6, "D"),
                (6, "H"),
                (6, "S"),
                (7, "C"),
                (7, "D"),
                (7, "H"),
                (7, "S"),
                (8, "C"),
                (8, "D"),
                (8, "H"),
                (8, "S"),
                (9, "C"),
                (9, "D"),
                (9, "H"),
                (9, "S"),
                (10, "C"),
                (10, "D"),
                (10, "H"),
                (10, "S"),
                ("J", "C"),
                ("J", "D"),
                ("J", "H"),
                ("J", "S"),
                ("Q", "C"),
                ("Q", "D"),
                ("Q", "H"),
                ("Q", "S"),
                ("K", "C"),
                ("K", "D"),
                ("K", "H"),
                ("K", "S"),
                ("A", "C"),
                ("A", "D"),
                ("A", "H"),
                ("A", "S"),
            ],
        )


if __name__ == "__main__":
    unittest.main()