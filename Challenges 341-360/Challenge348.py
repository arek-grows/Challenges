import unittest


def longest_word(sentence: str) -> str:
    sentence = sentence.split()
    l_word = ""
    l_length = 0
    for word in sentence:
        if (word_length := len(word)) > l_length:
            l_word = word
            l_length = word_length
    return l_word  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(longest_word("Hello darkness my old friend."), "darkness")

    def test_2(self):
        self.assertEqual(longest_word("Hello there mate."), "Hello")

    def test_3(self):
        self.assertEqual(longest_word("Margaret's toy is a pretty doll."), "Margaret's")

    def test_4(self):
        self.assertEqual(longest_word("A thing of beauty is a joy forever."), "forever.")

    def test_5(self):
        self.assertEqual(longest_word("Forgetfulness is by all means powerless!"), "Forgetfulness")

    def test_6(self):
        self.assertEqual(
            longest_word("The word 'strengths' is the longest and most commonly used word with a single vowel."),
            "'strengths'",
        )


if __name__ == "__main__":
    unittest.main()