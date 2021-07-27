import unittest


def reverse(message: str) -> str:
    new_message = ''
    for m in message:
        if m.isupper():
            new_message += m.lower()
        elif m.islower():
            new_message += m.upper()
        else:
            new_message += m
    return new_message[::-1]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("DLROw OLLEh", reverse("Hello World"))

    def test_2(self):
        self.assertEqual("eSrEvEr", reverse("ReVeRsE"))

    def test_3(self):
        self.assertEqual("", reverse(""))

    def test_4(self):
        self.assertEqual("RADAr", reverse("Radar"))


if __name__ == "__main__":
    unittest.main()