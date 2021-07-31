import unittest


def min_removals(string_a: str, string_b: str) -> int:
    setter = set(string_a + string_b)
    removals = 0
    for character in setter:
        # if a character is in string_a and string_b, the counts of the characters in the respective strings is
        # subtracted (equaling 0 if those characters are the same aka anagrams) and then added to removals.
        # else all other character counts are added to removals
        if character in string_a and character in string_b:
            removals += abs(string_a.count(character) - string_b.count(character))
        elif character in string_a:
            removals += string_a.count(character)
        elif character in string_b:
            removals += string_b.count(character)
    return removals  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, min_removals("abcde", "cab"))

    def test_2(self):
        self.assertEqual(2, min_removals("deafk", "kfeap"))

    def test_3(self):
        self.assertEqual(6, min_removals("abc", "ghi"))

    def test_4(self):
        self.assertEqual(7, min_removals("abcxyz", "ghixytz"))


if __name__ == "__main__":
    unittest.main()