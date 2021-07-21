import unittest


def halloween(date: str) -> str:
    if date[5:] == "10/31":
        return "Trick or Treat"
    return "Trick"  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("Trick or Treat", halloween("2013/10/31"))

    def test_2(self):
        self.assertEqual("Trick", halloween("2012/07/31"))

    def test_3(self):
        self.assertEqual("Trick or Treat", halloween("2015/10/31"))

    def test_4(self):
        self.assertEqual("Trick", halloween("2011/10/12"))

    def test_5(self):
        self.assertEqual("Trick", halloween("2008/10/11"))


if __name__ == "__main__":
    unittest.main()
