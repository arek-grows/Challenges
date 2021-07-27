import unittest


def profit_margin(cost_price: int, sales_price: int) -> str:
    return "%.1f%%" % ((sales_price - cost_price) / sales_price * 100)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("33.3%", profit_margin(10, 15))

    def test_2(self):
        self.assertEqual("-87.5%", profit_margin(75, 40))

    def test_3(self):
        self.assertEqual("0.0%", profit_margin(55, 55))

    def test_4(self):
        self.assertEqual("40.0%", profit_margin(30, 50))

    def test_5(self):
        self.assertEqual("0.0%", profit_margin(9999, 10001))

    def test_6(self):
        self.assertEqual("60.7%", profit_margin(33, 84))

    def test_7(self):
        self.assertEqual("28.2%", profit_margin(28, 39))


if __name__ == "__main__":
    unittest.main()