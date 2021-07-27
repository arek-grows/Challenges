from typing import List
import unittest


def get_discounts(values: List[int], discount: str) -> List[float]:
    discount = int(discount.replace('%', '')) / 100
    return [x * discount for x in values]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2, 3, 5.5], get_discounts([2, 4, 6, 11], "50%"))

    def test_2(self):
        self.assertEqual([7.5, 15, 30, 60], get_discounts([10, 20, 40, 80], "75%"))

    def test_3(self):
        self.assertEqual([45], get_discounts([100], "45%"))

    def test_4(self):
        self.assertEqual([0.2], get_discounts([20], "1%"))

    def test_5(self):
        self.assertEqual([5, 50, 500], get_discounts([100, 1000, 10000], "5%"))


if __name__ == "__main__":
    unittest.main()