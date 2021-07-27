import unittest


def double_letters(word: str) -> bool:
    previous_letter = word[0]
    for w in word[1:]:
        if previous_letter == w:
            return True
        else:
            previous_letter = w
    return False  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(double_letters("loop"))

    def test_2(self):
        self.assertTrue(double_letters("meeting"))

    def test_3(self):
        self.assertTrue(double_letters("yummy"))

    def test_4(self):
        self.assertTrue(double_letters("moo"))

    def test_5(self):
        self.assertTrue(double_letters("toodles"))

    def test_6(self):
        self.assertTrue(double_letters("droop"))

    def test_7(self):
        self.assertTrue(double_letters("loot"))

    def test_8(self):
        self.assertFalse(double_letters("orange"))

    def test_9(self):
        self.assertFalse(double_letters("munchkin"))

    def test_10(self):
        self.assertFalse(double_letters("forestry"))


if __name__ == "__main__":
    unittest.main()