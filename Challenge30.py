import unittest


def mystery_func(num: int) -> int:
    total = 1
    for n in str(num)[::-1]:
        total *= int(n)
    return total  # Put your code here!!!


class TestMysteryFunc(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mystery_func(152), 10)

    def test_2(self):
        self.assertEqual(mystery_func(832), 48)

    def test_3(self):
        self.assertEqual(mystery_func(5511), 25)

    def test_4(self):
        self.assertEqual(mystery_func(19), 9)

    def test_5(self):
        self.assertEqual(mystery_func(133), 9)

    def test_6(self):
        self.assertEqual(mystery_func(3456788919085693051928052), 0)

    def test_7(self):
        self.assertEqual(mystery_func(1234543234522542634), 1990656000)

    def test_8(self):
        self.assertEqual(mystery_func(1213141413121), 576)

    def test_9(self):
        self.assertEqual(mystery_func(987654321), 362880)

    def test_10(self):
        self.assertEqual(mystery_func(1234567890), 0)


if __name__ == "__main__":
    unittest.main()