import unittest


def is_letter_sum_even(string: str) -> bool:
    string = string.lower()
    # -96
    total = 0
    for ss in string:
        if ss.isalpha():
            total += ord(ss) - 96
    if total % 2 == 0:
        return True
    else:
        return False  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_letter_sum_even("i'am king"))

    def test_2(self):
        self.assertTrue(is_letter_sum_even("True"))

    def test_3(self):
        self.assertFalse(is_letter_sum_even("alexa"))


if __name__ == "__main__":
    unittest.main()