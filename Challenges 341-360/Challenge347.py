import unittest


def reversed_binary_integer(integer: int) -> int:
    integer = format(integer, 'b')
    integer = integer[::-1]
    integer = int(integer, 2)
    return integer  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reversed_binary_integer(1), 1)

    def test_2(self):
        self.assertEqual(reversed_binary_integer(4), 1)

    def test_3(self):
        self.assertEqual(reversed_binary_integer(5), 5)

    def test_4(self):
        self.assertEqual(reversed_binary_integer(31), 31)

    def test_5(self):
        self.assertEqual(reversed_binary_integer(82), 37)

    def test_6(self):
        self.assertEqual(reversed_binary_integer(90), 45)

    def test_7(self):
        self.assertEqual(reversed_binary_integer(255), 255)

    def test_8(self):
        self.assertEqual(reversed_binary_integer(446), 251)

    def test_9(self):
        self.assertEqual(reversed_binary_integer(451), 391)

    def test_10(self):
        self.assertEqual(reversed_binary_integer(634), 377)


if __name__ == "__main__":
    unittest.main()