import unittest


def steps_to_convert(text: str) -> int:
    steps = [0, 0]  # in the end, index 0 is how many steps for lower, index 1 for upper
    for t in text:
        if t.isupper():
            steps[0] += 1
        else:
            steps[1] += 1
    return min(steps)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, steps_to_convert("abC"))

    def test_2(self):
        self.assertEqual(2, steps_to_convert("abCBA"))

    def test_3(self):
        self.assertEqual(0, steps_to_convert("aba"))

    def test_4(self):
        self.assertEqual(0, steps_to_convert("ABA"))

    def test_5(self):
        self.assertEqual(3, steps_to_convert("abaCCC"))

    def test_6(self):
        self.assertEqual(4, steps_to_convert("abaaCCCDE"))

    def test_7(self):
        self.assertEqual(5, steps_to_convert("CCaaCCaaCa"))

    def test_8(self):
        self.assertEqual(0, steps_to_convert(""))


if __name__ == "__main__":
    unittest.main()