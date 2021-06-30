import unittest


def count_palindromes(range_start: int, range_end: int) -> int:
    total = 0
    for x in range(range_start, range_end + 1):
        total += 1 if str(x) == str(x)[::-1] else 0
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_palindromes(1, 10), 9)

    def test_2(self):
        self.assertEqual(count_palindromes(555, 556), 1)

    def test_3(self):
        self.assertEqual(count_palindromes(878, 898), 3)

    def test_4(self):
        self.assertEqual(count_palindromes(8, 34), 5)

    def test_5(self):
        self.assertEqual(count_palindromes(1550, 1556), 1)


if __name__ == "__main__":
    unittest.main()