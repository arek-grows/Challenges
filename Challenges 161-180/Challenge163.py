from typing import Optional, Union
import unittest


Number = Union[float, int]
Value = Optional[Number]


def ohms_law(v: Value = None, r: Value = None, i: Value = None) -> Union[Number, str]:
    if [v, r, i].count(None) != 1:
        return "Invalid"
    if v is None:
        return r * i
    elif r is None:
        return round(v / i, 2)
    elif i is None:
        return round(v / r, 2)
# Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(ohms_law(v=12, r=220), 0.05)

    def test_2(self):
        self.assertEqual(ohms_law(v=230, i=2), 115)

    def test_3(self):
        self.assertEqual(ohms_law(r=220, i=0.02), 4.4)

    def test_4(self):
        self.assertEqual(ohms_law(i=10), "Invalid")

    def test_5(self):
        self.assertEqual(ohms_law(v=500, r=50, i=10), "Invalid")


if __name__ == "__main__":
    unittest.main()