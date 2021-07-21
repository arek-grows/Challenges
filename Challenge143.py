from typing import Any, Optional
import unittest


def first_arg(*arg) -> Optional[Any]:
    if len(arg) == 0:
        return None
    return arg[0] # Put your code here!!!


def last_arg(*arg) -> Optional[Any]:
    if len(arg) == 0:
        return None
    return arg[-1] # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, first_arg(1, 2, 3))

    def test_2(self):
        self.assertEqual('a', first_arg('a', 'b', 'c'))

    def test_3(self):
        self.assertEqual(8, first_arg(8))

    def test_4(self):
        self.assertEqual(None, first_arg())

    def test_5(self):
        self.assertEqual(3, last_arg(1, 2, 3))

    def test_6(self):
        self.assertEqual('c', last_arg('a', 'b', 'c'))

    def test_7(self):
        self.assertEqual(8, last_arg(8))

    def test_8(self):
        self.assertEqual(None, last_arg())


if __name__ == "__main__":
    unittest.main()