import unittest


def neutralise(series_a: str, series_b: str) -> str:
    result = ''
    for a, b in zip(series_a, series_b):
        if a == b:
            result += a
        else:
            result += '0'
    return result  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(neutralise("--++--", "++--++"), "000000")

    def test_2(self):
        self.assertEqual(neutralise("-+-+-+", "-+-+-+"), "-+-+-+")

    def test_3(self):
        self.assertEqual(neutralise("-++-", "-+-+"), "-+00")

    def test_4(self):
        self.assertEqual(neutralise("--++", "++++"), "00++")

    def test_5(self):
        self.assertEqual(neutralise("+++--+---", "++----++-"), "++0--000-")

    def test_6(self):
        self.assertEqual(neutralise("-----", "-----"), "-----")

    def test_7(self):
        self.assertEqual(neutralise("-+", "++"), "0+")

    def test_8(self):
        self.assertEqual(neutralise("--", "-+"), "-0")

    def test_9(self):
        self.assertEqual(neutralise("-++", "+--"), "000")

    def test_10(self):
        self.assertEqual(neutralise("++-++--++-", "-+++-++-++"), "0+0+0000+0")

    def test_11(self):
        self.assertEqual(neutralise("-++-+-++-", "+-++++---"), "00+0+000-")

    def test_12(self):
        self.assertEqual(neutralise("---++-+--", "-+++--++-"), "-00+0-+0-")

    def test_13(self):
        self.assertEqual(neutralise("+-----+++-", "--+-+-++--"), "0-0-0-++0-")

    def test_14(self):
        self.assertEqual(neutralise("+-----+-", "---++-++"), "0--00-+0")

    def test_15(self):
        self.assertEqual(neutralise("-+--+-+---", "-+--+-+-+-"), "-+--+-+-0-")

    def test_16(self):
        self.assertEqual(neutralise("+-+", "-++"), "00+")

    def test_17(self):
        self.assertEqual(neutralise("-++", "-+-"), "-+0")

    def test_18(self):
        self.assertEqual(neutralise("---+", "-+++"), "-00+")

    def test_19(self):
        self.assertEqual(neutralise("+--", "+--"), "+--")

    def test_20(self):
        self.assertEqual(neutralise("--+++-+-", "+++++---"), "00+++-0-")


if __name__ == "__main__":
    unittest.main()