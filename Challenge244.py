import unittest


def oddish_or_evenish(number: int) -> str:
    ish = ['Evenish', 'Oddish']
    total = 0
    for n in str(number):
        total += int(n)
    return ish[total%2]  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(oddish_or_evenish(43), "Oddish")

    def test_2(self):
        self.assertEqual(oddish_or_evenish(373), "Oddish")

    def test_3(self):
        self.assertEqual(oddish_or_evenish(55551), "Oddish")

    def test_4(self):
        self.assertEqual(oddish_or_evenish(694), "Oddish")

    def test_5(self):
        self.assertEqual(oddish_or_evenish(4433), "Evenish")

    def test_6(self):
        self.assertEqual(oddish_or_evenish(11), "Evenish")

    def test_7(self):
        self.assertEqual(oddish_or_evenish(211112), "Evenish")


if __name__ == "__main__":
    unittest.main()