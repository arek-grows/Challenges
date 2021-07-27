# Challenge 199 - Days Until the End of the Month
#
# Create a function that takes the current date and returns the number of days until the end of the month.
# Examples
#
# days_to_months_end(date(2020, 2, 1)) -> 28
# days_to_months_end(date(1900, 2, 1)) -> 27
# days_to_months_end(date(2021, 3, 15)) -> 16
#
# Notes
#
#     Don't forget that leap years are every 4, but not every 100 except for every 400th year.


import unittest
from datetime import date
from calendar import monthrange


def days_to_months_end(current_date: date) -> int:
    days_in_month = monthrange(current_date.year, current_date.month)[1]
    return days_in_month - current_date.day  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            days_to_months_end(date(2020, 2, 1)),
            28,
        )

    def test_2(self):
        self.assertEqual(
            days_to_months_end(date(1900, 2, 1)),
            27,
        )

    def test_3(self):
        self.assertEqual(
            days_to_months_end(date(2021, 3, 15)),
            16,
        )

    def test_4(self):
        self.assertEqual(
            days_to_months_end(date(1, 1, 31)),
            0,
        )


if __name__ == "__main__":
    unittest.main()