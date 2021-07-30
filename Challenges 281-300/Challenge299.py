import unittest


def operation(operand_a: str, operand_b: str, operator: str) -> str:
    operations = {"add": "+", "divide": "//", "multiply": "*", "subtract": "-"}
    try:
        return str(eval(operand_a + operations[operator] + operand_b))  # Put your code here!!!
    except ZeroDivisionError:
        return "undefined"


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(operation("1", "2", "add"), "3")

    def test_2(self):
        self.assertEqual(operation("1", "-20", "add"), "-19")

    def test_3(self):
        self.assertEqual(operation("9", "0", "divide"), "undefined")

    def test_4(self):
        self.assertEqual(operation("10", "10", "multiply"), "100")

    def test_5(self):
        self.assertEqual(operation("-10", "-10", "multiply"), "100")

    def test_6(self):
        self.assertEqual(operation("10", "10", "subtract"), "0")

    def test_7(self):
        self.assertEqual(operation("0", "0", "subtract"), "0")

    def test_8(self):
        self.assertEqual(operation("0", "1", "divide"), "0")

    def test_9(self):
        self.assertEqual(operation("0", "25415", "divide"), "0")

    def test_10(self):
        self.assertEqual(
            operation(
                operation("10", "10", "multiply"),
                operation("10", "10", "add"),
                "divide",
            ),
            "5",
        )


if __name__ == "__main__":
    unittest.main()