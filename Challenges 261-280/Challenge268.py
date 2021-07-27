from __future__ import annotations
import unittest


def is_jackpot(result: tuple[str, str, str, str]) -> bool:
    result = set(result)
    return len(result) == 1  # Put your code here!!!


def is_jackpot_alt(result: tuple[str, str, str, str]) -> bool:
    return result.count(result[0]) == len(result)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_jackpot(("@", "@", "@", "@")))

    def test_2(self):
        self.assertTrue(is_jackpot(("!", "!", "!", "!")))

    def test_3(self):
        self.assertTrue(is_jackpot(("abc", "abc", "abc", "abc")))

    def test_4(self):
        self.assertTrue(is_jackpot(("karaoke", "karaoke", "karaoke", "karaoke")))

    def test_5(self):
        self.assertTrue(is_jackpot(("SS", "SS", "SS", "SS")))

    def test_6(self):
        self.assertFalse(is_jackpot((":(", ":)", ":|", ":|")))

    def test_7(self):
        self.assertFalse(is_jackpot(("&&", "&", "&&&", "&&&&")))

    def test_8(self):
        self.assertFalse(is_jackpot(("hee", "heh", "heh", "heh")))

    def test_9(self):
        self.assertFalse(is_jackpot(("SS", "SS", "SS", "Ss")))

    def test_10(self):
        self.assertFalse(is_jackpot(("SS", "SS", "Ss", "Ss")))


if __name__ == "__main__":
    unittest.main()