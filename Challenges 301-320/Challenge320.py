import unittest


def count_two_character_matches(string_a: str, string_b: str) -> int:
    total = 0
    for ii in range(min(len(string_a), len(string_b)) - 1):
        cons_a = string_a[ii] + string_a[ii + 1]
        cons_b = string_b[ii] + string_b[ii + 1]
        if cons_a == cons_b:
            total += 1
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_two_character_matches("jjcAAzz", "jjBAAz"), 3)

    def test_2(self):
        self.assertEqual(count_two_character_matches("ABcd", "ABcD"), 2)

    def test_3(self):
        self.assertEqual(count_two_character_matches("ABc", "Ajc"), 0)

    def test_4(self):
        self.assertEqual(count_two_character_matches("edabit", "ed"), 1)

    def test_5(self):
        self.assertEqual(count_two_character_matches("ed", "edabit"), 1)

    def test_6(self):
        self.assertEqual(count_two_character_matches("e", "edabit"), 0)

    def test_7(self):
        self.assertEqual(count_two_character_matches("", "edabit"), 0)

    def test_8(self):
        self.assertEqual(count_two_character_matches("AABBccDD", "ABBBjjD"), 1)

    def test_9(self):
        self.assertEqual(count_two_character_matches("AAjjAAjj", "iAjjAi"), 3)

    def test_10(self):
        self.assertEqual(count_two_character_matches("iAjjAi", "AAjjAAjj"), 3)


if __name__ == "__main__":
    unittest.main()