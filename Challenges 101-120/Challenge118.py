import unittest


def is_vowel_sandwich(word: str) -> bool:
    vowels = 'aeiou'
    if word[0] not in vowels and word[-1] not in vowels:
        for x in word[1:len(word) - 1]:
            if x not in vowels:
                return False
        return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_vowel_sandwich("cat"))

    def test_2(self):
        self.assertFalse(is_vowel_sandwich("ear"))

    def test_3(self):
        self.assertFalse(is_vowel_sandwich("bake"))

    def test_4(self):
        self.assertFalse(is_vowel_sandwich("fai"))

    def test_5(self):
        self.assertFalse(is_vowel_sandwich("eik"))

    def test_6(self):
        self.assertTrue(is_vowel_sandwich("nel"))

    def test_7(self):
        self.assertFalse(is_vowel_sandwich("lea"))

    def test_8(self):
        self.assertTrue(is_vowel_sandwich("rur"))

    def test_9(self):
        self.assertTrue(is_vowel_sandwich("zuh"))

    def test_10(self):
        self.assertFalse(is_vowel_sandwich("iiq"))


if __name__ == "__main__":
    unittest.main()