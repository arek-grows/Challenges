# Challenge 196 - Change Every Letter to the Next Letter
#
# Write a function that changes every letter to the next letter of the alphabet:
#
# "a" becomes "b"
# "b" becomes "c"
# "d" becomes "e"
# and so on ...
#
# Examples
#
# move("hello") ➞ "ifmmp"
#
# move("bye") ➞ "czf"
#
# move("welcome") ➞ "xfmdpnf"


import unittest


def move(word: str) -> str:
    alphabet = list(map(chr, range(97, 123)))
    back_reverse_alphabet = alphabet[1:] + alphabet[:1]
    moved = ''
    for x in word:
        moved += back_reverse_alphabet[alphabet.index(x)]
    return moved  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(move("hello"), "ifmmp")

    def test_2(self):
        self.assertEqual(move("lol"), "mpm")

    def test_3(self):
        self.assertEqual(move("bye"), "czf")

    def test_4(self):
        self.assertEqual(move("zebra"), "afcsb")


if __name__ == "__main__":
    unittest.main()