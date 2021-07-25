from __future__ import annotations
import unittest


def unique_abbreviations(abbreviations: list[str], words: list[str]) -> bool:
    for abbr in abbreviations:
        total = 0
        for word in words:
            if word[0:len(abbr)] == abbr:
                total += 1
        if total != 1:
            return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(
            unique_abbreviations(["s", "t", "v"], ["stamina", "television", "vindaloo"])
        )

    def test_2(self):
        self.assertTrue(
            unique_abbreviations(["mo", "ma", "me"], ["moment", "many", "mean"])
        )

    def test_3(self):
        self.assertTrue(
            unique_abbreviations(["at", "o", "abe"], ["atom", "original", "abet"])
        )

    def test_4(self):
        self.assertTrue(
            unique_abbreviations(["rh", "par", "re"], ["rhino", "parry", "residue"])
        )

    def test_5(self):
        self.assertFalse(
            unique_abbreviations(["ho", "h", "ha"], ["house", "hope", "happy"])
        )

    def test_6(self):
        self.assertFalse(
            unique_abbreviations(["bi", "ba", "bat"], ["big", "bard", "battery"])
        )

    def test_7(self):
        self.assertFalse(
            unique_abbreviations(["b", "c", "ch"], ["broth", "chap", "cardigan"])
        )

    def test_8(self):
        self.assertFalse(
            unique_abbreviations(["to", "too", "t"], ["topology", "took", "torrent"])
        )


if __name__ == "__main__":
    unittest.main()