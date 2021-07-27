# Challenge 204 - C*ns*r*d Str*ngs
#
# Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
#
# Given a censored string and a string of the censored vowels, return the original uncensored string.
# Example
#
# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
#
# uncensor("abcd", "") ➞ "abcd"
#
# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
#
# Notes
#
#     The vowels are given in the correct order.
#     The number of vowels will match the number of * characters in the censored string.


import unittest


def uncensor(censored: str, vowels: str) -> str:
    i = 0
    uncensored = ''
    for character in censored:
        if character == '*':
            character = vowels[i]
            i += 1
        uncensored += character
    return uncensored  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"), "Where did my vowels go?"
        )

    def test_2(self):
        self.assertEqual(uncensor("abcd", ""), "abcd")

    def test_3(self):
        self.assertEqual(uncensor("*PP*RC*S*", "UEAE"), "UPPERCASE")

    def test_4(self):
        self.assertEqual(
            uncensor("Ch**s*, Gr*mm*t -- ch**s*", "eeeoieee"),
            "Cheese, Grommit -- cheese",
        )

    def test_5(self):
        self.assertEqual(uncensor("*l*ph*nt", "Eea"), "Elephant")


if __name__ == "__main__":
    unittest.main()