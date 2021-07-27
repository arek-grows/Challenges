import unittest


def hamming_distance(string_1: str, string_2: str) -> int:
    total = 0
    for a, b in zip(string_1, string_2):
        if a != b:
            total += 1
    return total  # Put your code here!!!


class TestHammingDistance(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, hamming_distance("abcde", "bcdef"))

    def test_2(self):
        self.assertEqual(0, hamming_distance("abcde", "abcde"))

    def test_3(self):
        self.assertEqual(1, hamming_distance("strong", "strung"))

    def test_4(self):
        self.assertEqual(6, hamming_distance("foobar", "barfoo"))

    def test_5(self):
        self.assertEqual(6, hamming_distance("python", "golang"))

    def test_6(self):
        self.assertEqual(29, hamming_distance("This is a test, can you pass it?", "Did you fail this challenge?????"))


if __name__ == "__main__":
    unittest.main()