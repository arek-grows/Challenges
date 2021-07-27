# Challenge 195 - Letters Shared Between Two Words
#
# Create a function that returns the number of characters shared between two words.
# Examples
#
# shared_letters("apple", "meaty") ➞ 2
# # Since "ea" is shared between "apple" and "meaty".
#
# shared_letters("fan", "forsook") ➞ 1
#
# shared_letters("spout", "shout") ➞ 4


import unittest


def shared_letters(word_a: str, word_b: str) -> int:
    total = 0
    already = []
    for letter in word_a:
        if letter in already:
            pass
        elif letter in word_b:
            total += 1
            already.append(letter)
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(shared_letters("apple", "meaty"), 2)

    def test_2(self):
        self.assertEqual(shared_letters("fan", "forsook"), 1)

    def test_3(self):
        self.assertEqual(shared_letters("spout", "shout"), 4)

    def test_4(self):
        self.assertEqual(shared_letters("took", "taken"), 2)

    def test_5(self):
        self.assertEqual(shared_letters("mentor", "terminal"), 5)

    def test_6(self):
        self.assertEqual(shared_letters("class", "last"), 3)


if __name__ == "__main__":
    unittest.main()