import unittest


def leaps(start_year: int, end_year: int) -> int:
    counter = 0
    for year in range(start_year, end_year):
        if year % 4 == 0 and year % 100 != 0:
            counter += 1
        elif year % 100 == 0 and (year % 900 == 200 or year % 900 == 600):
            counter += 1
    return counter  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(leaps(2016, 2017), 1)

    def test_2(self):
        self.assertEqual(leaps(2019, 2020), 0)

    def test_3(self):
        self.assertEqual(leaps(1900, 1901), 0)

    def test_4(self):
        self.assertEqual(leaps(2000, 2001), 1)

    def test_5(self):
        self.assertEqual(leaps(2800, 2801), 0)

    def test_6(self):
        self.assertEqual(leaps(123456, 123456), 0)

    def test_7(self):
        self.assertEqual(leaps(1234, 5678), 1077)

    def test_8(self):
        self.assertEqual(leaps(123456, 7891011), 1881475)

    def test_9(self):
        self.assertEqual(leaps(123456789101112, 1314151617181920), 288412747246240)


if __name__ == "__main__":
    unittest.main()
