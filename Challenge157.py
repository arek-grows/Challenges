import unittest


def format_date(date: str) -> str:
    date = date.split("/")
    return "".join(date[::-1])  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(format_date("11/12/2019"), "20191211")

    def test_2(self):
        self.assertEqual(format_date("12/31/2019"), "20193112")

    def test_3(self):
        self.assertEqual(format_date("01/15/2019"), "20191501")


if __name__ == "__main__":
    unittest.main()