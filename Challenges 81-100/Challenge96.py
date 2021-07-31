from typing import Sequence, Union
import unittest


Literal = Union[int, str, bool]
LiteralSet = Sequence[Literal]


def validate_subsets(sets: Sequence[LiteralSet], super_set: LiteralSet) -> bool:
    for s in sets:
        for elem in s:
            if elem not in super_set:
                return False
    return True  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]))

    def test_2(self):
        self.assertTrue(validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]))

    def test_3(self):
        self.assertFalse(validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]))

    def test_4(self):
        self.assertFalse(validate_subsets([[1, 2, 3, 4]], [1, 2, 3]))

    def test_5(self):
        self.assertTrue(validate_subsets([['a', 'b'], ['b', 'c'], ['a', 'c']], ['a', 'b', 'c']))

    def test_6(self):
        self.assertTrue(validate_subsets([['a', 'b', 'c'], ['b'], ['c'], []], ['a', 'b', 'c']))

    def test_7(self):
        self.assertFalse(validate_subsets([['a', 'b'], ['b', 'c'], ['a', 'd']], ['a', 'b', 'c']))

    def test_8(self):
        self.assertFalse(validate_subsets([['a', 'b', 'c', 'd']], ['a', 'b', 'c']))

    def test_9(self):
        self.assertTrue(validate_subsets([[True, False], [True]], [True, False]))

    def test_10(self):
        self.assertTrue(validate_subsets([[True], [False], []], [True, False]))


if __name__ == "__main__":
    unittest.main()