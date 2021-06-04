# Challenge 221 - A Long Long Time
#
# Create a function that takes three values: • hours • minutes • seconds
#
# Return the value that's the longest duration.
# Examples
#
# longest_time(1, 59, 3598) ➞ 1
#
# longest_time(2, 300, 15000) ➞ 300
#
# longest_time(15, 955, 59400) ➞ 59400


import unittest


def longest_time(hours: int, minutes: int, seconds: int) -> int:
    times = [hours, minutes, seconds]
    times_s = [hours * 3600, minutes * 60, seconds]
    return times[times_s.index(max(times_s))]  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(longest_time(1, 59, 3598), 1)

    def test_2(self):
        self.assertEqual(longest_time(23, 0, 2000), 23)

    def test_3(self):
        self.assertEqual(longest_time(1, 65, 40), 65)

    def test_4(self):
        self.assertEqual(longest_time(0, 500, 4000), 500)

    def test_5(self):
        self.assertEqual(longest_time(5, 233, 9999999), 9999999)

    def test_6(self):
        self.assertEqual(longest_time(2, 955, 59400), 59400)


if __name__ == "__main__":
    unittest.main()