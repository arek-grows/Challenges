from __future__ import annotations
import unittest


def fruit_salad(fruits: list[str]) -> str:
    cut_fruits = []
    for fruit in fruits:
        cut_fruits.append(fruit[: int(len(fruit) / 2)])
        cut_fruits.append(fruit[int(len(fruit) / 2):])
    cut_fruits.sort()
    cut_string = ''
    for fruit in cut_fruits:
        cut_string += fruit
    return cut_string  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEquals(fruit_salad(['apple', 'pear', 'grapes']), 'apargrapepesple')

    def test_2(self):
        self.assertEquals(fruit_salad(['banana', 'kiwi', 'strawberry', 'blueberries']),
                          'anabanberryblueberrieskistrawwi')

    def test_3(self):
        self.assertEquals(fruit_salad(['raspberries', 'mango']), 'erriesmangoraspb')

    def test_4(self):
        self.assertEquals(fruit_salad(['banana']), 'anaban')


if __name__ == "__main__":
    unittest.main()
