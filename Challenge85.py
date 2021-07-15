import unittest


def valid_password(password: str) -> bool:
    if len(password) < 6:
        return False
    numbers = [str(x) for x in range(10)]
    contains_upper = False
    contains_lower = False
    contains_number = False
    for char in password:
        if char.isupper():
            contains_upper = True
        elif char.islower():
            contains_lower = True
        elif char in numbers:
            contains_number = True
        else:
            return False
        if contains_upper and contains_lower and contains_number:
            return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(valid_password("fjd3IR9"))

    def test_2(self):
        self.assertFalse(valid_password("ghdfj32"))

    def test_3(self):
        self.assertFalse(valid_password("DSJKHD23"))

    def test_4(self):
        self.assertFalse(valid_password("dsF43"))

    def test_5(self):
        self.assertTrue(valid_password("4fdg5Fj3"))

    def test_6(self):
        self.assertFalse(valid_password("DHSJdhjsU"))

    def test_7(self):
        self.assertFalse(valid_password("fjd3IR9.;"))

    def test_8(self):
        self.assertFalse(valid_password("fjd3  IR9"))

    def test_9(self):
        self.assertTrue(valid_password("djI38D55"))

    def test_10(self):
        self.assertFalse(valid_password("a2.d412"))

    def test_11(self):
        self.assertFalse(valid_password("JHD5FJ53"))

    def test_12(self):
        self.assertFalse(valid_password("!fdjn345"))

    def test_13(self):
        self.assertFalse(valid_password("jfkdfj3j"))

    def test_14(self):
        self.assertFalse(valid_password("123"))

    def test_15(self):
        self.assertFalse(valid_password("abc"))

    def test_16(self):
        self.assertTrue(valid_password("123abcABC"))

    def test_17(self):
        self.assertTrue(valid_password("ABC123abc"))

    def test_18(self):
        self.assertTrue(valid_password("Password123"))


if __name__ == "__main__":
    unittest.main()