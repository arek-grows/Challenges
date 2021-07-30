import unittest


def column(column_label: str) -> int:
    multiplier = 1
    total = 0
    for c in column_label[::-1]:
        total += (ord(c) - 64) * multiplier
        multiplier *= 26
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEquals(column("A"), 1)

    def test_2(self):
        self.assertEquals(column("B"), 2)

    def test_3(self):
        self.assertEquals(column("Z"), 26)

    def test_4(self):
        self.assertEquals(column("AA"), 27)

    def test_5(self):
        self.assertEquals(column("BA"), 53)

    def test_6(self):
        self.assertEquals(column("BB"), 54)

    def test_7(self):
        self.assertEquals(column("CW"), 101)

    def test_8(self):
        self.assertEquals(column("DD"), 108)

    def test_9(self):
        self.assertEquals(column("PQ"), 433)

    def test_10(self):
        self.assertEquals(column("ZZ"), 702)

    def test_11(self):
        self.assertEquals(column("ABC"), 731)

    def test_12(self):
        self.assertEquals(column("ZZT"), 18272)

    def test_13(self):
        self.assertEquals(column("STVW"), 348059)


if __name__ == "__main__":
    unittest.main()