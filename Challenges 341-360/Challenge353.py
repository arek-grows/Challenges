import unittest


def just_another_sum_problem(a: int, b: int) -> int:
    total = 0
    higher = b
    lower = a
    if a > b:
        higher = a
        lower = b

    # sum of 1 to n is (n * (n+1) / 2)
    # sum of -n to -1 is (n * (n-1) / -2)
    # for sum of a number > 1 to n:
    #   sum of 3 to 7: (7 * (7 + 1) / 2) - ((3 - 1) * 3 / 2)
    #                   (sum of 1 to 7) - (sum of 1 to 2)
    # for sum of -n to a number < -1:
    #   sum of -7 to -3: (-7 * (-7 - 1) / -2) - ((-3 + 1) * -3 / -2)
    #                   (sum of -7 to -1) - (sum of -2 to -1)

    # negative x, positive y
    if lower < 0 and higher > 0:
        # convert to float to int in case datatype is scientific notation
        return int(float(lower * (lower - 1) / -2)) + int(float(higher * (higher + 1) / 2))
    # x and y are negative
    elif lower < 0:
        return int(float(lower * (lower - 1) / -2)) - int(float((higher + 1) * higher / -2))
    # x and y are positive
    elif higher > 0:
        return int(float(higher * (higher + 1) / 2)) - int(float((lower - 1) * lower / 2))
    else:
        return "error"


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(just_another_sum_problem(1, -10), -54)

    def test_2(self):
        self.assertEqual(just_another_sum_problem(-20, 5), -195)

    def test_3(self):
        self.assertEqual(just_another_sum_problem(-40, 20), -610)

    def test_4(self):
        self.assertEqual(just_another_sum_problem(20, -100), -4840)

    def test_5(self):
        self.assertEqual(just_another_sum_problem(-15, 3), -114)

    def test_6(self):
        self.assertEqual(just_another_sum_problem(-8, 4), -26)

    def test_7(self):
        self.assertEqual(just_another_sum_problem(13, -1000000000), -500000000499999909)

    def test_8(self):
        self.assertEqual(just_another_sum_problem(7, 1000000000), 500000000499999979)

    def test_9(self):
        self.assertEqual(just_another_sum_problem(90, 45), 3105)

    def test_10(self):
        self.assertEqual(just_another_sum_problem(100, 58), 3397)


if __name__ == "__main__":
    unittest.main()