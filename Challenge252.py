import unittest


def shuffle_deck(cards: list) -> list:
    deck_one = cards[:len(cards)//2]
    deck_two = cards[len(cards)//2:]
    shuffled_deck = []
    for a, b in zip(deck_one, deck_two):
        shuffled_deck.append(a)
        shuffled_deck.append(b)
    return shuffled_deck


def shuffle_count(num_cards: int) -> int:
    original_deck = [i for i in range(1, num_cards+1)]
    shuffled_deck = shuffle_deck(original_deck)
    shuffles = 1
    while shuffled_deck != original_deck:
        shuffled_deck = shuffle_deck(shuffled_deck)
        shuffles += 1
    return shuffles  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(shuffle_count(2), 1)

    def test_2(self):
        self.assertEqual(shuffle_count(8), 3)

    def test_3(self):
        self.assertEqual(shuffle_count(14), 12)

    def test_4(self):
        self.assertEqual(shuffle_count(26), 20)

    def test_5(self):
        self.assertEqual(shuffle_count(52), 8)

    def test_6(self):
        self.assertEqual(shuffle_count(70), 22)

    def test_7(self):
        self.assertEqual(shuffle_count(104), 51)

    def test_8(self):
        self.assertEqual(shuffle_count(208), 66)


if __name__ == "__main__":
    unittest.main()