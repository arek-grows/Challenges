import unittest


def find_twice_age(fathers_age: int, sons_age: int) -> int:
    for x, (f, s) in enumerate(zip(range(fathers_age, fathers_age - sons_age, -1),
                                   range(sons_age, sons_age - sons_age, -1))):
        if s * 2 == f:
            return x
    for x, (f, s) in enumerate(zip(range(fathers_age, 101), range(sons_age, 101 + (fathers_age - sons_age)))):
        if s * 2 == f:
            return x
    return "error"  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_twice_age(36, 7), 22)

    def test_2(self):
        self.assertEqual(find_twice_age(55, 30), 5)

    def test_3(self):
        self.assertEqual(find_twice_age(42, 21), 0)

    def test_4(self):
        self.assertEqual(find_twice_age(22, 1), 20)

    def test_5(self):
        self.assertEqual(find_twice_age(29, 0), 29)


if __name__ == "__main__":
    unittest.main()