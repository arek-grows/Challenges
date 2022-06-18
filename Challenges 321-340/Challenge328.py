import unittest


def censor(string: str) -> str:
    string = string.split()
    end_string = []
    for word in string:
        if (length := len(word)) > 4:
            end_string.append("*" * length)
        else:
            end_string.append(word)
    return " ".join(end_string)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(censor("The code is fourty"), "The code is ******")

    def test_2(self):
        self.assertEqual(censor("Two plus three is five"), "Two plus ***** is five")

    def test_3(self):
        self.assertEqual(censor("aaaa aaaaa 1234 12345"), "aaaa ***** 1234 *****")

    def test_4(self):
        self.assertEqual(censor("abcdefghijklmnop"), "****************")

    def test_5(self):
        self.assertEqual(censor("a"), "a")


if __name__ == "__main__":
    unittest.main()