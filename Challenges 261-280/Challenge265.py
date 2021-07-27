import unittest


def count_matches(string_1: str, string_2: str) -> int:
    smallest_length = min(len(string_1), len(string_2))
    total = 0
    for i in range(smallest_length - 1):
        if string_1[i] + string_1[i + 1] == string_2[i] + string_2[i + 1]:
            total += 1
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_matches("jjcAAzz", "jjBAAz"), 3, "Some matches")

    def test_2(self):
        self.assertEqual(count_matches("ABcd", "ABcD"), 2, "case matters")

    def test_3(self):
        self.assertEqual(count_matches("ABc", "Ajc"), 0, "No matches")

    def test_4(self):
        self.assertEqual(count_matches("edabit", "ed"), 1, "B in A")

    def test_5(self):
        self.assertEqual(count_matches("ed", "edabit"), 1, "A in B")

    def test_6(self):
        self.assertEqual(count_matches("e", "edabit"), 0, "1 char is not a match")

    def test_7(self):
        self.assertEqual(count_matches("", "edabit"), 0, "Empty string check")

    def test_8(self):
        self.assertEqual(count_matches("AABBccDD", "ABBBjjD"), 1, "Random string")

    def test_9(self):
        self.assertEqual(count_matches("AAjjAAjj", "iAjjAi"), 3, "Random string")

    def test_10(self):
        self.assertEqual(count_matches("iAjjAi", "AAjjAAjj"), 3, "Random string")


if __name__ == "__main__":
    unittest.main()
