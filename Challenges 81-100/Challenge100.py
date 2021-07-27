import unittest


def card_hide(card_number: str) -> str:
    card_length = len(card_number)
    return ("*" * (card_length - 4)) + card_number[card_length - 4:]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("************5678", card_hide("1234123456785678"))

    def test_2(self):
        self.assertEqual("************3213", card_hide("8754456321113213"))

    def test_3(self):
        self.assertEqual("**********5523", card_hide("35123413355523"))


if __name__ == "__main__":
    unittest.main()