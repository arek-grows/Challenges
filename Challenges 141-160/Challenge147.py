import unittest


def emotify(sentence: str) -> str:
    word_emotes = {"smile": ":D", "grin": ":)", "sad": ":(", "mad": ":P"}
    sentence = sentence.split()
    for i, x in enumerate(sentence):
        if x in word_emotes:
            sentence[i] = word_emotes[x]
    return " ".join(sentence)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("Make me :D", emotify("Make me smile"))

    def test_2(self):
        self.assertEqual("Make me :)", emotify("Make me grin"))

    def test_3(self):
        self.assertEqual("Make me :(", emotify("Make me sad"))

    def test_4(self):
        self.assertEqual("Make me :P", emotify("Make me mad"))


if __name__ == "__main__":
    unittest.main()