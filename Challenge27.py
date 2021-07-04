import unittest
from typing import List


def is_shifted(list_a: List[int], list_b: List[int]) -> bool:
    shifted_by = list_b[0] - list_a[0]
    for a, b in zip(list_a, list_b):
        if a + shifted_by != b:
            return False
    return True  # Replace with your code!


def is_multiplied(list_a: List[int], list_b: List[int]) -> bool:
    multiplied_by = 0
    if sum(list_b) == 0:
        return True
    elif 0 in list_b:
        return False
    else:
        multiplied_by = list_b[0] / list_a[0]
    for a, b in zip(list_a, list_b):
        if a * multiplied_by != b:
            return False
    return True  # Replace with your code!


class TestValidators(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_shifted([1, 2, 3], [2, 3, 4]), True)

    def test_2(self):
        self.assertEqual(is_shifted([1, 2, 3], [-9, -8, -7]), True)

    def test_3(self):
        self.assertEqual(is_multiplied([1, 2, 3], [10, 20, 30]), True)

    def test_4(self):
        self.assertEqual(is_multiplied([1, 2, 3], [-0.5, -1, -1.5]), True )

    def test_5(self):
        self.assertEqual(is_multiplied([1, 2, 3], [0, 0, 0]), True )

    def test_6(self):
        self.assertEqual(is_shifted([1, 2, 3], [2, 3, 5]), False)

    def test_7(self):
        self.assertEqual(is_shifted([1, 2, 3], [-9, -1, -7]), False)

    def test_8(self):
        self.assertEqual(is_multiplied([1, 2, 3], [10, 20, 29]), False)

    def test_9(self):
        self.assertEqual(is_multiplied([1, 2, 3], [-0.5, -1, -2]), False)

    def test_10(self):
        self.assertEqual(is_multiplied([1, 2, 3], [0, 0, 1]), False)


if __name__ == "__main__":
    unittest.main()