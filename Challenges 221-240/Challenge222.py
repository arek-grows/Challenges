# Challenge 222 - Simplified Fractions
#
# Create a function that returns the simplified version of a fraction.
# Examples
#
# simplify("4/6") ➞ "2/3"
#
# simplify("10/11") ➞ "10/11"
#
# simplify("100/400") ➞ "1/4"
#
# simplify("8/4") ➞ "2"
#
# Notes
#
# A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. For
# example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor. If improper fractions can be transformed
# into integers, do so in your code


import unittest


def simplify(fraction: str) -> str:
    b_slash = fraction.index('/')
    nr_1 = int(fraction[:b_slash])
    nr_2 = int(fraction[b_slash + 1:])
    if nr_1 % nr_2 == 0:
        return str(int(nr_1/nr_2))
    if nr_1 > nr_2:
        smallest = nr_2
    else:
        smallest = nr_1
    hcf = 0
    for x in range(1, smallest + 1):
        if nr_1 % x == 0 and nr_2 % x == 0:
            hcf = x
    simplified_fraction = str(int(nr_1/hcf)) + '/' + str(int(nr_2/hcf))
    return simplified_fraction  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(simplify("5/7"), "5/7")

    def test_2(self):
        self.assertEqual(simplify("4/6"), "2/3")

    def test_3(self):
        self.assertEqual(simplify("11/10"), "11/10")

    def test_4(self):
        self.assertEqual(simplify("8/4"), "2")

    def test_5(self):
        self.assertEqual(simplify("7/4"), "7/4")

    def test_6(self):
        self.assertEqual(simplify("6/4"), "3/2")

    def test_7(self):
        self.assertEqual(simplify("300/200"), "3/2")

    def test_8(self):
        self.assertEqual(simplify("50/25"), "2")

    def test_9(self):
        self.assertEqual(simplify("5/45"), "1/9")


if __name__ == "__main__":
    unittest.main()