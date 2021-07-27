import unittest


def get_groups(groups: int, years: int) -> str:
    end = []
    for x in range(1, years + 1):
        for y in range(1, groups + 1):
            end.append(str(x) + chr(96 + y))
    return ", ".join(end)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            "1a, 1b, 1c, 1d, 1e, "
            "2a, 2b, 2c, 2d, 2e, "
            "3a, 3b, 3c, 3d, 3e, "
            "4a, 4b, 4c, 4d, 4e, "
            "5a, 5b, 5c, 5d, 5e, "
            "6a, 6b, 6c, 6d, 6e",
            get_groups(5, 6)
        )

    def test_2(self):
        self.assertEqual(
            "1a, 2a",
            get_groups(1, 2)
        )

    def test_3(self):
        self.assertEqual(
            "1a",
            get_groups(1, 1)
        )

    def test_4(self):
        self.assertEqual(
            "1a, 1b, 1c, 1d",
            get_groups(4, 1)
        )

    def test_5(self):
        self.assertEqual(
            "1a, 1b, 1c, "
            "2a, 2b, 2c, "
            "3a, 3b, 3c",
            get_groups(3, 3)
        )

if __name__ == "__main__":
    unittest.main()