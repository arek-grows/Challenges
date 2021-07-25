from __future__ import annotations
import unittest


def same_vowel_group(words: list[str]) -> list[str]:
    end_list = [words[0]]
    vowels = "aeiou"
    need_vowels = ""
    for v in vowels:
        if v in end_list[0]:
            need_vowels += v
    for word in words[1:]:
        in_word = True
        for v in vowels:
            if v not in need_vowels and v in word:  # if vowel isn't in first word and is in current looped word
                in_word = False
                break
            elif v in need_vowels and v not in word:  # if vowel is in first but not in current looped word
                in_word = False
                break
        if in_word:
            end_list.append(word)
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(
            same_vowel_group(["hoops", "chuff", "bot", "bottom"]),
            ["hoops", "bot", "bottom"],
        )

    def test_2(self):
        self.assertListEqual(
            same_vowel_group(["crop", "nomnom", "bolo", "yodeller"]),
            ["crop", "nomnom", "bolo"],
        )

    def test_3(self):
        self.assertListEqual(
            same_vowel_group(["semantic", "aimless", "beautiful", "meatless icecream"]),
            ["semantic", "aimless", "meatless icecream"],
        )

    def test_4(self):
        self.assertListEqual(
            same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]),
            ["many"],
        )

    def test_5(self):
        self.assertListEqual(
            same_vowel_group(["toe", "ocelot", "maniac"]), ["toe", "ocelot"]
        )

    def test_6(self):
        self.assertListEqual(
            same_vowel_group(["a", "apple", "flat", "map", "shark"]),
            ["a", "flat", "map", "shark"],
        )

    def test_7(self):
        self.assertListEqual(
            same_vowel_group(["a", "aa", "ab", "abc", "aaac", "abe"]),
            ["a", "aa", "ab", "abc", "aaac"],
        )


if __name__ == "__main__":
    unittest.main()