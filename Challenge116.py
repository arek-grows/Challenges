from typing import List
import unittest


def to_list(number: int) -> List[int]:
    number = str(number)
    end = []
    for x in number:
        end.append(int(x))
    return end  # Put your code here!!!


def to_number(place_values: List[int]) -> int:
    end = ''
    for x in place_values:
        end += str(x)
    return int(end)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual([2, 3, 5], to_list(235))

    def test_2(self):
        self.assertEqual([1, 9], to_list(19))

    def test_3(self):
        self.assertEqual([0], to_list(0))

    def test_4(self):
        self.assertEqual(235, to_number([2, 3, 5]))

    def test_5(self):
        self.assertEqual(19, to_number([1, 9]))

    def test_6(self):
        self.assertEqual(0, to_number([0]))


if __name__ == "__main__":
    unittest.main()