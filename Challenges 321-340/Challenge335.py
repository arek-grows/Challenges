import unittest


def math_expr(string: str) -> bool:
    try:
        end = eval(string)
    except:
        return False
    return True  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(math_expr("5+4"))

    def test_2(self):
        self.assertTrue(math_expr("4 * 5"))

    def test_3(self):
        self.assertTrue(math_expr("3*6"))

    def test_4(self):
        self.assertTrue(math_expr("4 - 5"))

    def test_5(self):
        self.assertTrue(math_expr("6 % 7"))

    def test_6(self):
        self.assertFalse(math_expr("a - b"))

    def test_7(self):
        self.assertFalse(math_expr("a - 2"))

    def test_8(self):
        self.assertFalse(math_expr("nope"))


if __name__ == "__main__":
    unittest.main()