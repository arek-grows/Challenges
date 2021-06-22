import unittest


def square_digits(number: int) -> int:
    number = str(number)
    total = ''
    for n in number:
        total += str(int(n) ** 2)
    return int(total)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(square_digits(9119), 811181)

    def test_2(self):
        self.assertEqual(square_digits(8726), 6449436)

    def test_3(self):
        self.assertEqual(square_digits(9763), 8149369)

    def test_4(self):
        self.assertEqual(square_digits(2230), 4490)

    def test_5(self):
        self.assertEqual(square_digits(2797), 4498149)


if __name__ == "__main__":
    unittest.main()