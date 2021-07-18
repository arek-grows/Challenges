import unittest


def is_valid_pin(pin: str) -> bool:
    if len(pin) == 4 or len(pin) == 6:
        try:
            pin = int(pin)
        except ValueError:
            return False
    else:
        return False
    return True  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_valid_pin("1234"))

    def test_2(self):
        self.assertFalse(is_valid_pin("12345"))

    def test_3(self):
        self.assertFalse(is_valid_pin("a234"))

    def test_4(self):
        self.assertFalse(is_valid_pin(""))

    def test_5(self):
        self.assertFalse(is_valid_pin("%234"))

    def test_6(self):
        self.assertFalse(is_valid_pin("`234"))

    def test_7(self):
        self.assertFalse(is_valid_pin("@234"))

    def test_8(self):
        self.assertFalse(is_valid_pin("#234"))

    def test_9(self):
        self.assertFalse(is_valid_pin("$234"))

    def test_10(self):
        self.assertFalse(is_valid_pin("*234"))


if __name__ == "__main__":
    unittest.main()