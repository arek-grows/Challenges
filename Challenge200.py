# Challenge 200 - Free Throw Probability
#
# What's the probability of someone making a certain amount of free throws in a row given their free throw success percentage? If Sally makes 50% of her free shot throws. Then Sally's probability of making 5 in a row would be 3%.
# Examples
#
# free_throws("75%", 5) ➞ "24%"
#
# free_throws("25%", 3) ➞ "2%"
#
# free_throws("90%", 30) ➞ "4%"
#
# Notes
#
#     Round your answer to the nearest whole number.
#     percent ** rounds


import unittest


def free_throws(probability: str, throws: int) -> str:
    probability = int(probability.replace('%', '')) / 100
    return str(round((probability ** throws) * 100)) + '%'  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(free_throws("50%", 5), "3%")

    def test_2(self):
        self.assertEqual(free_throws("75%", 10), "6%")

    def test_3(self):
        self.assertEqual(free_throws("25%", 3), "2%")

    def test_4(self):
        self.assertEqual(free_throws("90%", 30), "4%")


if __name__ == "__main__":
    unittest.main()