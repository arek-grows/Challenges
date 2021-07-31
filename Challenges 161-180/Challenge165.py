import unittest


def double_factorial(num: int) -> int:
    end = 1
    for x in range(num, 0, -2):
        end *= x
    return end  # Put your code here!!!


def double_factorial_alt(num: int) -> int:
    end = 1
    while num > 0:
        end *= num
        num -= 2
    return end  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(double_factorial(-1), 1)

    def test_2(self):
        self.assertEqual(double_factorial(0), 1)

    def test_3(self):
        self.assertEqual(double_factorial(1), 1)

    def test_4(self):
        self.assertEqual(double_factorial(2), 2)

    def test_5(self):
        self.assertEqual(double_factorial(7), 105)

    def test_6(self):
        self.assertEqual(double_factorial(9), 945)

    def test_7(self):
        self.assertEqual(double_factorial(14), 645120)

    def test_8(self):
        self.assertEqual(double_factorial(22), 81749606400)

    def test_9(self):
        self.assertEqual(double_factorial(25), 7905853580625)

    def test_10(self):
        self.assertEqual(double_factorial(27), 213458046676875)


if __name__ == "__main__":
    unittest.main()