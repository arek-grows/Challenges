import unittest


def parse_int(number: str) -> int:
    numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 6, "eight": 8,
               "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
               "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "fourty": 40,
               "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
    multipliers = {"hundred": 100, "thousand": 1_000, "million": 1_000_000}
    number = number.split()
    total = 0
    return 0  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, parse_int('one'))

    def test_2(self):
        self.assertEqual(20, parse_int('twenty'))

    def test_3(self):
        self.assertEqual(246, parse_int('two hundred forty-six'))


if __name__ == "__main__":
    unittest.main()