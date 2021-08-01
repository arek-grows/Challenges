from typing import Union
import unittest


def to_underscore(name: Union[str, int]) -> str:
    if type(name) is not str:
        return str(name)
    if len(name) < 2:
        return str(name).lower()
    snake_case = name[0].lower()
    for x in name[1:]:
        if x.isupper() or x.isdigit():
            snake_case += "_" + x.lower()
        else:
            snake_case += x
    return snake_case  # Put your code here!!!


class TestToUnderscore(unittest.TestCase):
    def test_1(self):
        self.assertEqual(to_underscore("TestController"), "test_controller")

    def test_2(self):
        self.assertEqual(to_underscore('MoviesAndBooks'), "movies_and_books")

    def test_3(self):
        self.assertEqual(to_underscore('App7Test'), "app_7_test")

    def test_4(self):
        self.assertEqual(to_underscore(1), "1")


if __name__ == "__main__":
    unittest.main()