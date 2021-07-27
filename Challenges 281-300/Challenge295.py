from __future__ import annotations
from typing import Union
import unittest


def fizz_buzz(maximum: int) -> list[Union[int, str]]:
    end_list = []
    for x in range(1, maximum + 1):
        fizzy_buzzer = ""
        if x % 3 == 0:
            fizzy_buzzer += "Fizz"
        if x % 5 == 0:
            fizzy_buzzer += "Buzz"
        if not fizzy_buzzer:
            end_list.append(x)
        else:
            end_list.append(fizzy_buzzer)
    return end_list  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(fizz_buzz(10), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'])

    def test_2(self):
        self.assertListEqual(
            fizz_buzz(15),
            [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        )


if __name__ == "__main__":
    unittest.main()