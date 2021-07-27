import unittest


def to_scottish_screaming(words: str) -> str:
    vowels = 'AIOU'
    words = words.upper()
    for v in vowels:
        words = words.replace(v, "E")
    return words  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(to_scottish_screaming("lorem ipsum"), "LEREM EPSEM")

    def test_2(self):
        self.assertEqual(to_scottish_screaming("Leeroy jenkins!"), "LEEREY JENKENS!")

    def test_3(self):
        self.assertEqual(
            to_scottish_screaming("A, wonderful, day, don't, you, think?"),
            "E, WENDERFEL, DEY, DEN'T, YEE, THENK?",
        )

    def test_4(self):
        self.assertEqual(to_scottish_screaming("Hello world"), "HELLE WERLD")

    def test_5(self):
        self.assertEqual(
            to_scottish_screaming("start queueing you oafs"), "STERT QEEEEENG YEE EEFS"
        )


if __name__ == "__main__":
    unittest.main()