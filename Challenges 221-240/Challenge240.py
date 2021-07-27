from typing import Union
import unittest


def stupid_addition(first_number: Union[int, str], second_number: Union[int, str]) -> Union[int, str]:
    if type(first_number) != type(second_number):
        return None
    elif type(first_number) == int:
        first_number = str(first_number)
        second_number = str(second_number)
    else:
        first_number = int(first_number)
        second_number = int(second_number)
    return first_number + second_number  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(stupid_addition(1, 2), "12")

    def test_2(self):
        self.assertEqual(stupid_addition("1", "2"), 3)

    def test_3(self):
        self.assertEqual(stupid_addition(1, "2"), None)

    def test_4(self):
        self.assertEqual(stupid_addition("1", 2), None)


if __name__ == "__main__":
    unittest.main()
