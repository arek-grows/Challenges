import unittest


def sum_of_vowels(string: str) -> int:
    vowel_val = {"A": 4, "E": 3, "I": 1}
    string = string.upper()
    total = 0
    for ss in string:
        if ss in vowel_val:
            total += vowel_val[ss]
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_of_vowels("Let's test this function."), 8)

    def test_2(self):
        self.assertEqual(sum_of_vowels("Do I get the correct output?"), 10)

    def test_3(self):
        self.assertEqual(sum_of_vowels("Will you still need me, will you still feed me when I'm 64?"), 26)

    def test_4(self):
        self.assertEqual(
            sum_of_vowels("The greatest glory in living lies not in never falling, but in rising every time we fall."),
            52
        )


if __name__ == "__main__":
    unittest.main()