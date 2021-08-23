import unittest


def arithmetic_operation(equation: str) -> int:
    try:
        return eval(equation)
    except ZeroDivisionError:
        return -1


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(arithmetic_operation("12 + 12"), 24)

    def test_2(self):
        self.assertEqual(arithmetic_operation("22 - 12"), 10)

    def test_3(self):
        self.assertEqual(arithmetic_operation("100 * 12"), 1200)

    def test_4(self):
        self.assertEqual(arithmetic_operation("120 / 10"), 12)

    def test_5(self):
        self.assertEqual(arithmetic_operation("122 / 0"), -1)

    def test_6(self):
        self.assertEqual(arithmetic_operation("10 * 20"), 200)

    def test_7(self):
        self.assertEqual(arithmetic_operation("10 - 10"), 0)

    def test_8(self):
        self.assertEqual(arithmetic_operation("10 - 12"), -2)


if __name__ == "__main__":
    unittest.main()