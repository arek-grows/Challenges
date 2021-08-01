import unittest


def calculator(num_1: int, operator: str, num_2: int) -> int:
    try:
        return int(eval(str(num_1) + operator + str(num_2)))
    except ZeroDivisionError:
        return "Can't divide by 0!"  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, calculator(2, '/', 2))

    def test_2(self):
        self.assertEqual(3, calculator(10, '-', 7))

    def test_3(self):
        self.assertEqual(32, calculator(2, '*', 16))

    def test_4(self):
        self.assertEqual(0, calculator(2, '-', 2))

    def test_5(self):
        self.assertEqual(41, calculator(15, '+', 26))

    def test_6(self):
        self.assertEqual(4, calculator(2, '+', 2))

    def test_7(self):
        self.assertEqual("Can't divide by 0!", calculator(2, "/", 0))

    def test_8(self):
        self.assertIsInstance(calculator(3, "/", 2), int)


if __name__ == "__main__":
    unittest.main()