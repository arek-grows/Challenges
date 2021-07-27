from __future__ import annotations
import unittest


def get_primiera_score(deck: list[str]) -> int:
    suits = ['d', 'h', 'c', 's']
    point_dict = {"A": 16, "2": 12, "3": 13, "4": 14, "5": 15, "6": 18, "7": 21, "J": 10, "Q": 10, "K": 10}

    values = [[0], [0], [0], [0]]
    primiera = 0
    for card in deck:
        suit = card[1:]
        value = card[:1]
        values[suits.index(suit)].append(point_dict[value])
    for v in values:
        if max(v) == 0:
            return 0
        else:
            primiera += max(v)
    return primiera  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_primiera_score(["3d", "6d", "6h", "Qh", "7s", "As", "6c", "Jc"]), 75)

    def test_2(self):
        self.assertEqual(get_primiera_score(["3d", "7d", "Kd", "7h", "Qh", "Ah", "7s", "3c", "Jc"]), 76)

    def test_3(self):
        self.assertEqual(get_primiera_score(["5d", "7h", "Qc", "Ac", "4c", "Kc", "As"]), 68)

    def test_4(self):
        self.assertEqual(
            get_primiera_score(["7d", "Ad", "Kd", "2h", "6h", "5h", "Ah", "3c", "Jc", "Ac", "7c", "3c", "4c"]),
            0
        )


if __name__ == "__main__":
    unittest.main()