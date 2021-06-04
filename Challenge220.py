# Challenge 220 - Capital Split
#
# Create a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.
# Examples
#
# cap_space("helloWorld") ➞ "hello world"
#
# cap_space("iLoveMyTeapot") ➞ "i love my teapot"
#
# cap_space("stayIndoors") ➞ "stay indoors"


import unittest
import re


def cap_space(string: str) -> str:
    caps = re.findall('[A-Z]', string)
    phrase = string[:string.index(caps[0])]
    for x in range(1, len(caps)):
        word = string[string.index(caps[x - 1]):string.index(caps[x])]
        phrase += ' ' + word.lower()
    phrase += ' ' + string[string.index(caps[len(caps) - 1]):].lower()
    return phrase  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cap_space("helloWorld"), "hello world")

    def test_2(self):
        self.assertEqual(cap_space("iLoveMyTeapot"), "i love my teapot")

    def test_3(self):
        self.assertEqual(cap_space("stayIndoors"), "stay indoors")


if __name__ == "__main__":
    unittest.main()
