import unittest


def is_harshad(number: int) -> bool:
    try:
        return number % sum([int(x) for x in str(number)]) == 0  # Put your code here!!!
    except ZeroDivisionError:
        return False


class Test(unittest.TestCase):
    def test_1(self):
        self.assertFalse(is_harshad(0))

    def test_2(self):
        self.assertFalse(is_harshad(15))

    def test_3(self):
        self.assertTrue(is_harshad(990))

    def test_4(self):
        self.assertFalse(is_harshad(461))

    def test_5(self):
        self.assertFalse(is_harshad(297))

    def test_6(self):
        self.assertFalse(is_harshad(345))

    def test_7(self):
        self.assertFalse(is_harshad(529))

    def test_8(self):
        self.assertFalse(is_harshad(839))

    def test_9(self):
        self.assertFalse(is_harshad(281))

    def test_10(self):
        self.assertTrue(is_harshad(252))


if __name__ == "__main__":
    unittest.main()