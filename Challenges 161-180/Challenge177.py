import unittest


def reversible_inclusive_list(start: int, end: int) -> list:
    nr_list = []
    order = 1
    if start > end:
        order = -1
    for a in range(start, end + order, order):
        nr_list.append(a)
    return nr_list  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reversible_inclusive_list(5, 1), [5, 4, 3, 2, 1])

    def test_2(self):
        self.assertEqual(reversible_inclusive_list(6, 2), [6, 5, 4, 3, 2])

    def test_3(self):
        self.assertEqual(
            reversible_inclusive_list(10, 20),
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        )

    def test_4(self):
        self.assertEqual(
            reversible_inclusive_list(24, 17), [24, 23, 22, 21, 20, 19, 18, 17]
        )

    def test_5(self):
        self.assertEqual(
            reversible_inclusive_list(40, 50),
            [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
        )

    def test_6(self):
        self.assertEqual(
            reversible_inclusive_list(51, 41),
            [51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41],
        )

    def test_7(self):
        self.assertEqual(
            reversible_inclusive_list(11, 66),
            [
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46,
                47,
                48,
                49,
                50,
                51,
                52,
                53,
                54,
                55,
                56,
                57,
                58,
                59,
                60,
                61,
                62,
                63,
                64,
                65,
                66,
            ],
        )

    def test_8(self):
        self.assertEqual(reversible_inclusive_list(9, 3), [9, 8, 7, 6, 5, 4, 3])

    def test_9(self):
        self.assertEqual(
            reversible_inclusive_list(6, 16), [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        )


if __name__ == "__main__":
    unittest.main()