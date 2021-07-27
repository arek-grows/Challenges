import unittest
import re


def count_same_ends(sentence: str) -> int:
    sentence = sentence.lower()
    sentence = re.sub("[^A-Za-z\s]+", "", sentence)
    words = sentence.split()
    total = 0
    for word in words:
        if word[0] == word[-1] and len(word) > 1:
            total += 1
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_same_ends("Pop! the balloon!"), 1)

    def test_2(self):
        self.assertEqual(count_same_ends("My mom is not a nun."), 2)

    def test_3(self):
        self.assertEqual(count_same_ends("A fine morning"), 0)

    def test_4(self):
        self.assertEqual(count_same_ends("And the crowd goes wild!"), 0)

    def test_5(self):
        self.assertEqual(count_same_ends("No I am not in a gang."), 1)

    def test_6(self):
        self.assertEqual(count_same_ends("Taste the difference"), 0)


if __name__ == "__main__":
    unittest.main()