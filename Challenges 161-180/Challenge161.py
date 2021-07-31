from typing import Callable, TypeVar
import unittest


T = TypeVar("T", int, float)


def adds_n(amount: int) -> Callable[[T], T]:
    return lambda x: amount + x  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        adds1 = adds_n(1)
        self.assertEqual(adds1(3), 4)
        self.assertEqual(adds1(5.7), 6.7)

    def test_2(self):
        adds10 = adds_n(10)
        self.assertEqual(adds10(44), 54)
        self.assertEqual(adds10(20), 30)

    def test_3(self):
        adds5neg = adds_n(-5)
        self.assertEqual(adds5neg(0), -5)
        self.assertEqual(adds5neg(77), 72)

    def test_4(self):
        adds0 = adds_n(0)
        self.assertEqual(adds0(77), 77)


if __name__ == "__main__":
    unittest.main()