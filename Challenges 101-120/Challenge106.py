import unittest


def can_alternate(binary: str) -> bool:
    if len(binary) > 0 and abs(binary.count('1') - binary.count('0')) < 2:
        return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(can_alternate("0001111"))

    def test_2(self):
        self.assertTrue(can_alternate("01001"))

    def test_3(self):
        self.assertFalse(can_alternate("010001"))

    def test_4(self):
        self.assertFalse(can_alternate("0100110111"))

    def test_5(self):
        self.assertTrue(can_alternate("10101010"))

    def test_6(self):
        self.assertFalse(can_alternate("010101000"))

    def test_7(self):
        self.assertFalse(can_alternate("0111"))

    def test_8(self):
        self.assertFalse(can_alternate("00"))

    def test_9(self):
        self.assertFalse(can_alternate("1111"))

    def test_10(self):
        self.assertTrue(can_alternate("101"))


if __name__ == "__main__":
    unittest.main()