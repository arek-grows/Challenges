import unittest


def arithmetic_arranger(problems, is_displayed=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # create each line as a list. each list will have strings that will be joined by 4 whitespaces in the end
    line_one = []  # first operands
    line_two = []  # operator + second operands
    dashes_line = []  # dashes
    totals_line = []  # answers to the problems

    for prob in problems:
        # expecting prob to be something like "1 + 2" aka first operator_sign second, after split
        split_prob = prob.split()

        if len(split_prob) != 3:
            return "Error: Invalid evaluation string."

        first_operand, operator_sign, second_operand = split_prob
        first_length = len(first_operand)
        second_length = len(second_operand)

        # errors
        if operator_sign != '+' and operator_sign != '-':
            return "Error: Operator must be '+' or '-'."
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        if first_length > 4 or second_length > 4:
            return "Error: Numbers cannot be more than four digits."

        # the total length of each line is the length of the longest operand + 2
        line_length = max([first_length, second_length]) + 2
        # add the appropriate amount of spaces to each string and then append to the line lists, to be joined later
        # number of spaces to add == line_length - length of the operand on that line
        line_one.append((" " * (line_length - first_length)) + first_operand)
        # operator sign takes a space so minus 1 from line_length
        line_two.append((operator_sign + " " * (line_length - second_length - 1)) + second_operand)
        # append line_length * dashes to the dashes line
        dashes_line.append("-" * line_length)

        if is_displayed:
            # Considering the error checks before this, prob will be a number, + or -, and another number so I don't
            # expect eval() to be abusable in this situation
            total = str(eval(prob))
            totals_line.append((" " * (line_length - len(total))) + total)

    four_spaces = " " * 4
    # join each line list with four_spaces
    line_one = four_spaces.join(line_one)
    line_two = four_spaces.join(line_two)
    dashes_line = four_spaces.join(dashes_line)

    # put the joined strings into a list in order to join with a new character line later
    arranged_problems = [line_one, line_two, dashes_line]

    if is_displayed:
        # join and append totals_line to end list if we want to display it
        totals_line = four_spaces.join(totals_line)
        arranged_problems.append(totals_line)

    arranged_problems = "\n".join(arranged_problems)

    return arranged_problems


# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected,
                         'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected,
                         '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')

    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(actual, expected,
                         'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected,
                         'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(actual, expected,
                         'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithmetic problems and a second argument of `True`.')


if __name__ == "__main__":
    unittest.main()
