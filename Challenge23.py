import unittest
from typing import AnyStr


def compute(instructions: AnyStr) -> int:
    stack = []
    computations = {"DUP": "stack.append(stack[-1])",
                    "POP": "stack.pop()",
                    "+": "new_value = stack.pop()\n"
                         "stack.append(new_value + stack.pop())",
                    "-": "new_value = []\n"
                         "new_value.append(stack.pop())\n"
                         "new_value.append(stack.pop())\n"
                         "stack.append(max(new_value) - min(new_value))",
                    "*": "new_value = stack.pop()\n"
                         "stack.append(new_value * stack.pop())",
                    "/": "new_value = []\n"
                         "new_value.append(stack.pop())\n"
                         "new_value.append(stack.pop())\n"
                         "stack.append(max(new_value) / min(new_value))"}

    instructions = instructions.split()
    for i in instructions:
        if i.isdigit():
            stack.append(int(i))
        elif i in computations:
            exec(computations[i])
        else:
            return "Invalid instruction: %s" % i
    if len(stack) == 0:
        return 0
    # Your code here
    return stack[-1]


class TestCalculator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute('12'), 12)

    def test_2(self):
        self.assertEqual(compute('5 6 +'), 11)

    def test_3(self):
        self.assertEqual(compute('3 6 -'), 3)

    def test_4(self):
        self.assertEqual(compute('3 DUP +'), 6)

    def test_5(self):
        self.assertEqual(compute('2 5 - 5 + DUP +'), 16)

    def test_6(self):
        self.assertEqual(compute('9 14 DUP + - 3 POP'), 19)

    def test_7(self):
        self.assertEqual(compute('1 2 3 4 5 POP POP POP'), 2)

    def test_8(self):
        self.assertEqual(compute('13 DUP 4 POP 5 DUP + DUP + -'), 7)

    def test_9(self):
        self.assertEqual(compute('6 5 5 7 * - /'), 5)

    def test_10(self):
        self.assertEqual(compute('4 2 4 * 3 + 5 + / 5 -'), 1)

    def test_11(self):
        self.assertEqual(compute('5 8 + 4 5 1 + POP 13 +'), 17)

    def test_12(self):
        self.assertEqual(compute('x'), 'Invalid instruction: x')

    def test_13(self):
        self.assertEqual(compute('4 6 + x'), 'Invalid instruction: x')

    def test_14(self):
        self.assertEqual(compute('y x *'), 'Invalid instruction: y')

    def test_15(self):
        self.assertEqual(compute(''), 0)

    def test_16(self):
        self.assertEqual(compute('4 POP'), 0)


if __name__ == "__main__":
    unittest.main()