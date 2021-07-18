import unittest


def happiness_number(string: str) -> int:
    smile_points = {":)": 1, "(:": 1, ":(": -1, "):": -1}
    total = 0
    for smiles in smile_points:
        total += string.count(smiles) * smile_points[smiles]
    return total  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(-1, happiness_number(':):('))

    def test_2(self):
        self.assertEqual(2, happiness_number('(:)'))

    def test_3(self):
        self.assertEqual(0, happiness_number('::::'))

    def test_4(self):
        self.assertEqual(-2, happiness_number(':)::(()::'))

    def test_5(self):
        self.assertEqual(-1, happiness_number('))):'))

    def test_6(self):
        self.assertEqual(1, happiness_number(':):)('))

    def test_7(self):
        self.assertEqual(-2, happiness_number(':(:(:()):'))

    def test_8(self):
        self.assertEqual(-1, happiness_number('()((:())):'))

    def test_9(self):
        self.assertEqual(1, happiness_number(':(:)'))

    def test_10(self):
        self.assertEqual(2, happiness_number('(:):(:)(('))


if __name__ == "__main__":
    unittest.main()