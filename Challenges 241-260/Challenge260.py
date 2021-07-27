import unittest
import math


def get_number_of_apples(apples: int, eaten: str) -> int:
    eaten = int(eaten[:len(eaten)-1])
    apples_eaten = math.ceil(apples * (eaten * 0.01))
    children_apples = apples - apples_eaten
    if children_apples == 0:
        children_apples = "The children didn't get any apples"
    return children_apples  # Put your code here!!!`


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_number_of_apples(10, "90%"), 1)

    def test_2(self):
        self.assertEqual(get_number_of_apples(25, "10%"), 22)

    def test_3(self):
        self.assertEqual(
            get_number_of_apples(0, "10%"), "The children didn't get any apples"
        )

    def test_4(self):
        self.assertEqual(get_number_of_apples(40, "30%"), 28)

    def test_5(self):
        self.assertEqual(get_number_of_apples(10, "44%"), 5)

    def test_6(self):
        self.assertEqual(
            get_number_of_apples(12, "100%"), "The children didn't get any apples"
        )

    def test_7(self):
        self.assertEqual(
            get_number_of_apples(40, "100%"), "The children didn't get any apples"
        )


if __name__ == "__main__":
    unittest.main()