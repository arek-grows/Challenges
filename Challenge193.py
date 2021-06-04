# Challenge 193 - Decode The Seven Segment Digits
#
# Create a program to decode a seven segment display, commonly seen on many older electronic devices.
#
# Your decode_digits function will receive a string that has 3 lines, with each line being 27 characters long (representing 9 total numbers), with the digits spread across the 3 lines. Your job is to return the represented digits. You don't need to account for odd spacing or missing segments. Return the integer number represented by the seven segment digits.
# Example
#
# digits = """
#     _  _     _  _  _  _  _
#   | _| _||_||_ |_   ||_||_|
#   ||_  _|  | _||_|  ||_| _|
# """
# decode_digits(digits) -> 123456789


import unittest


def decode_digits(digits: str) -> int:
    digitized_numbers = [' _ | ||_|', '     |  |', ' _  _||_ ', ' _  _| _|', '   |_|  |', ' _ |_  _|', ' _ |_ |_|',
                         ' _   |  |', ' _ |_||_|', ' _ |_| _|']
    numbers = ''
    digits = digits.replace('\n', '')
    for i in range(0, 27, 3):
        number = ''
        for a in range(0, 81, 27):
            number += digits[i+a] + digits[i+a+1] + digits[i+a+2]
        numbers += str(digitized_numbers.index(number))
    return int(numbers)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        digits = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""
        self.assertEqual(decode_digits(digits), 123456789)

    def test_2(self):
        digits = """
    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|
"""
        self.assertEqual(decode_digits(digits), 433805825)

    def test_3(self):
        digits = """
 _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|
"""
        self.assertEqual(decode_digits(digits), 526837608)

    def test_4(self):
        digits = """
 _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ 
"""
        self.assertEqual(decode_digits(digits), 954105592)


if __name__ == "__main__":
    unittest.main()