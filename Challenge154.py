import unittest


def validate_pin(pin: str) -> bool:
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    return False  # Put your code here!!!


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(validate_pin("123456"), True)

    def test_2(self):
        self.assertEqual(validate_pin("4512a5"), False)

    def test_3(self):
        self.assertEqual(validate_pin(""), False)

    def test_4(self):
        self.assertEqual(validate_pin("21904"), False)

    def test_5(self):
        self.assertEqual(validate_pin("9451"), True)

    def test_6(self):
        self.assertEqual(validate_pin("213132"), True)

    def test_7(self):
        self.assertEqual(validate_pin(" 4520"), False)

    def test_8(self):
        self.assertEqual(validate_pin("15632 "), False)

    def test_9(self):
        self.assertEqual(validate_pin("000000"), True)


if __name__ == "__main__":
    unittest.main()