# Challenge 207 - Parentheses Clusters
#
# Write a function that groups a string into parentheses cluster. Each cluster should be balanced.
# Examples
#
# split("()()()") ➞ ["()", "()", "()"]
#
# split("((()))") ➞ ["((()))"]
#
# split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]
#
# split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
#
# Notes
#
#     All input strings will only contain parentheses.
#     Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.


import unittest


def split(parentheses: str):
    b, e = 0, 0
    current = ''
    end = []
    for character in parentheses:
        current += character
        if character == '(':
            b += 1
        else:
            e += 1
        if b == e:
            end.append(current)
            current = ''
            b, e = 0, 0
    return end  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(split("()()()"), ["()", "()", "()"])

    def test_2(self):
        self.assertEqual(split(""), [])

    def test_3(self):
        self.assertEqual(split("()()(())"), ["()", "()", "(())"])

    def test_4(self):
        self.assertEqual(split("(())(())"), ["(())", "(())"])

    def test_5(self):
        self.assertEqual(split("((()))"), ["((()))"])

    def test_6(self):
        self.assertEqual(
            split("()(((((((((())))))))))"), ["()", "(((((((((())))))))))"]
        )

    def test_7(self):
        self.assertEqual(
            split("((())()(()))(()(())())(()())"),
            ["((())()(()))", "(()(())())", "(()())"],
        )

    def test_8(self):
        self.assertEqual(
            split("((()))(())()()(()())"), ["((()))", "(())", "()", "()", "(()())"]
        )

    def test_9(self):
        self.assertEqual(split("((())())(()(()()))"), ["((())())", "(()(()()))"])

    def test_10(self):
        self.assertEqual(
            split("(()(()()))()(((()))()(()))(()((()))(())())"),
            ["(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"],
        )


if __name__ == "__main__":
    unittest.main()