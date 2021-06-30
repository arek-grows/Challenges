import unittest


def loves_me(num_petals: int) -> str:
    love_list = ['Loves me']
    for x in range(1, num_petals):
        if x % 2 == 0:
            love_list.append('Loves me')
        else:
            love_list.append('Loves me not')
    love_list[-1] = love_list[-1].upper()
    return ", ".join(love_list)  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(loves_me(1), "LOVES ME")

    def test_2(self):
        self.assertEqual(loves_me(2), "Loves me, LOVES ME NOT")

    def test_3(self):
        self.assertEqual(loves_me(3), "Loves me, Loves me not, LOVES ME")

    def test_4(self):
        self.assertEqual(loves_me(4), "Loves me, Loves me not, Loves me, LOVES ME NOT")

    def test_5(self):
        self.assertEqual(
            loves_me(5), "Loves me, Loves me not, Loves me, Loves me not, LOVES ME"
        )

    def test_6(self):
        self.assertEqual(
            loves_me(6),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT",
        )

    def test_7(self):
        self.assertEqual(
            loves_me(7),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, LOVES ME",
        )

    def test_8(self):
        self.assertEqual(
            loves_me(8),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT",
        )

    def test_9(self):
        self.assertEqual(
            loves_me(9),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, LOVES ME",
        )

    def test_10(self):
        self.assertEqual(
            loves_me(10),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, "
            "LOVES ME NOT",
        )

    def test_11(self):
        self.assertEqual(
            loves_me(11),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, "
            "Loves me not, LOVES ME",
        )

    def test_12(self):
        self.assertEqual(
            loves_me(12),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, "
            "Loves me not, Loves me, LOVES ME NOT",
        )

    def test_13(self):
        self.assertEqual(
            loves_me(13),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, "
            "Loves me not, Loves me, Loves me not, LOVES ME",
        )

    def test_14(self):
        self.assertEqual(
            loves_me(14),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, "
            "Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT",
        )

    def test_15(self):
        self.assertEqual(
            loves_me(15),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, Loves me, "
            "Loves me not, Loves me, Loves me not, Loves me, Loves me not, LOVES ME",
        )


if __name__ == "__main__":
    unittest.main()