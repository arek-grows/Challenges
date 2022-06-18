import unittest


def get_drink_id(string: str, capacity: str) -> str:
    string = string.split()
    drink_id = ""
    for ss in string:
        drink_id += ss[:3].upper()
    drink_id += capacity.replace("ml", "")
    return drink_id  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_drink_id("apple", "500ml"), "APP500")

    def test_2(self):
        self.assertEqual(get_drink_id("pineapple", "45ml"), "PIN45")

    def test_3(self):
        self.assertEqual(get_drink_id("orange", "750ml"), "ORA750")

    def test_4(self):
        self.assertEqual(get_drink_id("passion fruit", "1ml"), "PASFRU1")

    def test_5(self):
        self.assertEqual(get_drink_id("mango", "1000ml"), "MAN1000")

    def test_6(self):
        self.assertEqual(get_drink_id("very berry", "253ml"), "VERBER253")

    def test_7(self):
        self.assertEqual(get_drink_id("raspberry and lime", "350ml"), "RASANDLIM350")


if __name__ == "__main__":
    unittest.main()