import unittest


def can_build(letters: str, string: str) -> bool:
    letters = list(letters)
    try:
        for s in string:
            letters.remove(s)
    except ValueError:
        return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(can_build("aPPleAL", "PAL"))

    def test_2(self):
        self.assertTrue(can_build("OAT", "OAT"))

    def test_3(self):
        self.assertTrue(can_build("maybelLINE", "maybe"))

    def test_4(self):
        self.assertTrue(can_build("topsh", "shop"))

    def test_5(self):
        self.assertTrue(can_build("topshSHP", "SHoP"))

    def test_16(self):
        self.assertFalse(can_build("a", "aA"))

    def test_17(self):
        self.assertFalse(can_build("a", "A"))

    def test_18(self):
        self.assertFalse(can_build("AAAAAA", "AAAAAAa"))

    def test_19(self):
        self.assertFalse(can_build("apple", "appleY"))

    def test_20(self):
        self.assertFalse(can_build("xxYYzZ", "zzZxYxY"))

    def test_21(self):
        self.assertFalse(can_build("abCD", "aBCD"))


if __name__ == "__main__":
    unittest.main()