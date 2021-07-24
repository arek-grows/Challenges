import unittest


def ascii_compare(word_a: str, word_b: str) -> str:
    totals = {word_a: 0, word_b: 0}
    for a in word_a:
        totals[word_a] += ord(a)
    for b in word_b:
        totals[word_b] += ord(b)
    return min(totals, key=totals.get)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("man", ascii_compare("hey", "man"))

    def test_2(self):
        self.assertEqual("then", ascii_compare("majorly", "then"))

    def test_3(self):
        self.assertEqual("magic", ascii_compare("magic", "kingdom"))

    def test_4(self):
        self.assertEqual("bored", ascii_compare("bored", "shampoo"))

    def test_5(self):
        self.assertEqual("victory", ascii_compare("victory", "careless"))


if __name__ == "__main__":
    unittest.main()