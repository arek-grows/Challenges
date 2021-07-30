import unittest


class Name:
    def __init__(self, first: str, last: str):
        """Put your code here!!!"""
        self.fname = first.capitalize()
        self.lname = last.capitalize()
        self.fullname = self.fname + " " + self.lname
        self.initials = self.fname[0] + "." + self.lname[0]


class Tests(unittest.TestCase):
    def setUp(self):
        # super().__init__()
        self.a1 = Name("john", "SMITH")
        self.a2 = Name("sARah", "fRolliE")

    def test_1(self):
        self.assertEqual(self.a1.fname, "John")

    def test_2(self):
        self.assertEqual(self.a1.lname, "Smith")

    def test_3(self):
        self.assertEqual(self.a1.fullname, "John Smith")

    def test_4(self):
        self.assertEqual(self.a1.initials, "J.S")

    def test_5(self):
        self.assertEqual(self.a2.fname, "Sarah")

    def test_6(self):
        self.assertEqual(self.a2.lname, "Frollie")

    def test_7(self):
        self.assertEqual(self.a2.fullname, "Sarah Frollie")

    def test_8(self):
        self.assertEqual(self.a2.initials, "S.F")


if __name__ == "__main__":
    unittest.main()
