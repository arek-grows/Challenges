# Challenge 198 - Alphabet Cipher
#
# "The Alphabet Cipher", published by Lewis Carroll in 1868, describes a Vigenère cipher for passing secret messages. The cipher involves alphabet substitution using a shared keyword. Using the alphabet cipher to transmit messages follows this procedure:
#
# You must make a substitution chart like this, where each row of the alphabet is rotated by one as each letter goes down the chart. All test cases will utilize this same substitution chart.
#
#   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# A abcdefghijklmnopqrstuvwxyz
# B bcdefghijklmnopqrstuvwxyza
# C cdefghijklmnopqrstuvwxyzab
# D defghijklmnopqrstuvwxyzabc
# E efghijklmnopqrstuvwxyzabcd
# F fghijklmnopqrstuvwxyzabcde
# G ghijklmnopqrstuvwxyzabcdef
# H hijklmnopqrstuvwxyzabcdefg
# I ijklmnopqrstuvwxyzabcdefgh
# J jklmnopqrstuvwxyzabcdefghi
# K klmnopqrstuvwxyzabcdefghij
# L lmnopqrstuvwxyzabcdefghijk
# M mnopqrstuvwxyzabcdefghijkl
# N nopqrstuvwxyzabcdefghijklm
# O opqrstuvwxyzabcdefghijklmn
# P pqrstuvwxyzabcdefghijklmno
# Q qrstuvwxyzabcdefghijklmnop
# R rstuvwxyzabcdefghijklmnopq
# S stuvwxyzabcdefghijklmnopqr
# T tuvwxyzabcdefghijklmnopqrs
# U uvwxyzabcdefghijklmnopqrst
# V vwxyzabcdefghijklmnopqrstu
# W wxyzabcdefghijklmnopqrstuv
# X xyzabcdefghijklmnopqrstuvw
# Y yzabcdefghijklmnopqrstuvwx
# Z zabcdefghijklmnopqrstuvwxy
#
# Both people exchanging messages must agree on the secret keyword. To encode the message, first write it down.
#
# thepackagehasbeendelivered
#
# Then, write the keyword, (for example, snitch), repeated as many times as necessary.
#
# snitchsnitchsnitchsnitchsn
# thepackagehasbeendelivered
#
# Now you can look up the column S in the table and follow it down until it meets the T row. The value at the intersection is the letter L. All the letters would be thus encoded.
#
# snitchsnitchsnitchsnitchsn  # Key
# thepackagehasbeendelivered  # Message
# lumicjcnoxjhkomxpkwyqogywq  # Encoded
#
# The encoded message is now lumicjcnoxjhkomxpkwyqogywq
#
# To decode, the other person would use the secret keyword and the table to look up the letters in reverse.
#
# Create a function that takes a keyword and message parameter and returns the encoded message.
# Examples
#
# alphabet_cipher("snitch", "thepackagehasbeendelivered") -> "lumicjcnoxjhkomxpkwyqogywq"
# alphabet_cipher("bond", "theredfoxtrotsquietlyatmidnight") -> "uvrufrsryherugdxjsgozogpjralhvg"
# alphabet_cipher("train", "murderontheorientexpress") -> "flrlrkfnbuxfrqrgkefckvsa"
# alphabet_cipher("garden", "themolessnuckintothegardenlastnight") -> "zhvpsyksjqypqiewsgnexdvqkncdwgtixkx"


import unittest
from itertools import cycle


def rotate(l, n):
    return l[n:] + l[:n]


def create_substitution_chart():
    alphabet = list(map(chr, range(97, 123)))
    sub_chart = []
    for i in range(26):
        sub_chart.append(alphabet)
        alphabet = rotate(alphabet, 1)
    return sub_chart, alphabet


def alphabet_cipher(keyword: str, message: str) -> str:
    sub_chart, alphabet = create_substitution_chart()
    encoded = ''
    key = ''
    message_len = len(message)
    i_keyword = cycle(keyword)
    for i, x in zip(range(message_len), i_keyword):
        key += x
    for a, b in zip(key, message):
        encoded += sub_chart[alphabet.index(b)][alphabet.index(a)]
    return encoded  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            alphabet_cipher("snitch", "thepackagehasbeendelivered"),
            "lumicjcnoxjhkomxpkwyqogywq",
        )

    def test_2(self):
        self.assertEqual(
            alphabet_cipher("bond", "theredfoxtrotsquietlyatmidnight"),
            "uvrufrsryherugdxjsgozogpjralhvg",
        )

    def test_3(self):
        self.assertEqual(
            alphabet_cipher("train", "murderontheorientexpress"),
            "flrlrkfnbuxfrqrgkefckvsa",
        )

    def test_4(self):
        self.assertEqual(
            alphabet_cipher("garden", "themolessnuckintothegardenlastnight"),
            "zhvpsyksjqypqiewsgnexdvqkncdwgtixkx",
        )


if __name__ == "__main__":
    unittest.main()
