import unittest


def is_central(string: str) -> bool:
    if (str_len := len(string)) % 2 == 0:
        return False
    elif string[str_len // 2] != " ":
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_central("  #  "))

    def test_2(self):
        self.assertFalse(is_central(" 2    "))

    def test_3(self):
        self.assertTrue(is_central("@"))

    def test_4(self):
        self.assertFalse(is_central(" 1"))

    def test_5(self):
        self.assertFalse(is_central("7 "))

    def test_6(self):
        self.assertFalse(is_central("  l "))

    def test_7(self):
        self.assertFalse(is_central(" a  "))

    def test_8(self):
        self.assertTrue(is_central("    G    "))

    def test_9(self):
        self.assertFalse(is_central("   G     "))

    def test_10(self):
        self.assertTrue(is_central("        %        "))


if __name__ == "__main__":
    unittest.main()