import unittest


def gimme_the_letters(letter_range: str) -> str:
    end_string = ""
    for ii in range(ord(letter_range[0]), ord(letter_range[-1]) + 1):
        end_string += chr(ii)
    return end_string  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(gimme_the_letters("a-z"), "abcdefghijklmnopqrstuvwxyz")

    def test_2(self):
        self.assertEqual(gimme_the_letters("h-o"), "hijklmno")

    def test_3(self):
        self.assertEqual(gimme_the_letters("Q-Z"), "QRSTUVWXYZ")

    def test_4(self):
        self.assertEqual(gimme_the_letters("J-J"), "J")

    def test_5(self):
        self.assertEqual(gimme_the_letters("a-b"), "ab")

    def test_6(self):
        self.assertEqual(gimme_the_letters("A-A"), "A")

    def test_7(self):
        self.assertEqual(gimme_the_letters("g-i"), "ghi")

    def test_8(self):
        self.assertEqual(gimme_the_letters("H-I"), "HI")

    def test_9(self):
        self.assertEqual(gimme_the_letters("y-z"), "yz")

    def test_10(self):
        self.assertEqual(gimme_the_letters("e-k"), "efghijk")


if __name__ == "__main__":
    unittest.main()