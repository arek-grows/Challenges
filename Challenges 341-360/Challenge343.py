import unittest


def club_entry(word: str) -> int:
    for ii in range(len(word)):
        if word[ii] == word[ii + 1]:
            return (ord(word[ii]) - 96) * 4
    return 0  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(club_entry("lettuce"), 80)

    def test_2(self):
        self.assertEqual(club_entry("hill"), 48)

    def test_3(self):
        self.assertEqual(club_entry("apple"), 64)

    def test_4(self):
        self.assertEqual(club_entry("addiction"), 16)

    def test_5(self):
        self.assertEqual(club_entry("bee"), 20)

    def test_6(self):
        self.assertEqual(club_entry("zz"), 104)

    def test_7(self):
        self.assertEqual(club_entry("mubashirr"), 72)


if __name__ == "__main__":
    unittest.main()