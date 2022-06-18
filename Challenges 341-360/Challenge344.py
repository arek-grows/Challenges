import unittest


def percentage_changed(old_price: str, new_price: str) -> str:
    old_price = old_price.replace("$", "")
    new_price = new_price.replace("$", "")
    old_price, new_price = int(old_price), int(new_price)
    change = new_price/old_price
    if change == 1:
        return "no change"
    # increase
    elif change > 1:
        increase = round((change - 1) * 100)
        return f"{increase}% increase"
    # decrease
    else:
        decrease = round((1 - change) * 100)
        return f"{decrease}% decrease"


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(percentage_changed("$800", "$600"), "25% decrease")

    def test_2(self):
        self.assertEqual(percentage_changed("$1000", "$840"), "16% decrease")

    def test_3(self):
        self.assertEqual(percentage_changed("$700", "$650"), "7% decrease")

    def test_4(self):
        self.assertEqual(percentage_changed("$100", "$950"), "850% increase")

    def test_5(self):
        self.assertEqual(percentage_changed("$450", "$460"), "2% increase")

    def test_6(self):
        self.assertEqual(percentage_changed("$1000", "$1500"), "50% increase")


if __name__ == "__main__":
    unittest.main()