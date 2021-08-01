import unittest


def which_are_true(first: bool, second: bool) -> str:
    truth_matrix = [["neither", "second"], ["first", "both"]]
    return truth_matrix[first][second]  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("both", which_are_true(True, True))

    def test_2(self):
        self.assertEqual("first", which_are_true(True, False))

    def test_3(self):
        self.assertEqual("second", which_are_true(False, True))

    def test_4(self):
        self.assertEqual("neither", which_are_true(False, False))


if __name__ == "__main__":
    unittest.main()