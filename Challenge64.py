import unittest


def special_reverse(phrase: str, starting_letter: str) -> str:
    phrase = phrase.split()
    for x, p in enumerate(phrase):
        if p[0] == starting_letter:
            phrase[x] = p[::-1]
    return " ".join(phrase)  # Pout your code here!!!


class TestSpecialReverse(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            "word sehcraes are repus fun",
            special_reverse("word searches are super fun", "s"),
        )

    def test_2(self):
        self.assertEqual(
            "first nam to walk on the noom",
            special_reverse("first man to walk on the moon", "m"),
        )

    def test_3(self):
        self.assertEqual(
            "retep repip dekcip delkcip sreppep",
            special_reverse("peter piper picked pickled peppers", "p"),
        )

    def test_4(self):
        self.assertEqual(
            "he went to climb mount everest",
            special_reverse("he went to climb mount everest", "p"),
        )


if __name__ == "__main__":
    unittest.main()