import unittest


def extend_vowels(word: str, extend: int) -> str:
    if extend < 0 or type(extend) == float:
        return "invalid"
    if extend == 0:
        return word
    end_string = ""
    vowels = "aeiou"
    for ss in word:
        end_string += ss
        if ss.lower() in vowels:
            end_string += ss * extend
    return end_string  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(extend_vowels("Hello", 5), "Heeeeeelloooooo")

    def test_2(self):
        self.assertEqual(extend_vowels("Beginner.py", 3), "Beeeegiiiinneeeer.py")

    def test_3(self):
        self.assertEqual(extend_vowels("Extend", 0), "Extend")

    def test_4(self):
        self.assertEqual(extend_vowels("A", 10), "AAAAAAAAAAA")

    def test_5(self):
        self.assertEqual(extend_vowels("Z", 93), "Z")

    def test_6(self):
        self.assertEqual(extend_vowels("Vowel", 0.5), "invalid")

    def test_7(self):
        self.assertEqual(extend_vowels("Nice", -8), "invalid")


if __name__ == "__main__":
    unittest.main()