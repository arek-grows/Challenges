import unittest


def palindromic_date(date: str) -> bool:
    date = date.replace('/', '')
    date_two = date[2:4] + date[0:2] + date[4:]
    if (date == date[::-1]) and (date_two == date_two[::-1]):
        return True
    return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(palindromic_date("02/02/2020"))

    def test_2(self):
        self.assertFalse(palindromic_date("11/12/2019"))

    def test_3(self):
        self.assertFalse(palindromic_date("11/02/2011"))

    def test_4(self):
        self.assertFalse(palindromic_date("06/10/1469"))

    def test_5(self):
        self.assertFalse(palindromic_date("06/05/3133"))

    def test_6(self):
        self.assertTrue(palindromic_date("12/12/2121"))

    def test_7(self):
        self.assertTrue(palindromic_date("09/09/9090"))

    def test_8(self):
        self.assertFalse(palindromic_date("11/04/2203"))

    def test_9(self):
        self.assertTrue(palindromic_date("07/07/7070"))

    def test_10(self):
        self.assertFalse(palindromic_date("06/11/2923"))

    def test_11(self):
        self.assertFalse(palindromic_date("03/08/8030"))

    def test_12(self):
        self.assertTrue(palindromic_date("01/01/1010"))

    def test_13(self):
        self.assertFalse(palindromic_date("03/11/3369"))

    def test_14(self):
        self.assertFalse(palindromic_date("11/03/2775"))

    def test_15(self):
        self.assertFalse(palindromic_date("03/03/1822"))


if __name__ == "__main__":
    unittest.main()