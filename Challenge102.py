from typing import List, Tuple
import unittest


def where_is_waldo(grid: List[List[str]]) -> Tuple[int, int]:
    for x, a in enumerate(grid, start=1):
        if len(set(a)) == 2:
            elems = list(set(a))
            if a.count(elems[0]) == 1:
                odd_one_out = elems[0]
            else:
                odd_one_out = elems[1]
            for y, b in enumerate(a, start=1):
                if b == odd_one_out:
                    return x, y


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            (3, 2), where_is_waldo([["A", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]])
        )

    def test_2(self):
        self.assertEqual(
            (2, 4), where_is_waldo([["c", "c", "c", "c"], ["c", "c", "c", "d"]])
        )

    def test_3(self):
        self.assertEqual(
            (5, 1),
            where_is_waldo(
                [
                    ["O", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                    ["P", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                ]
            ),
        )

    def test_4(self):
        self.assertEqual(
            (1, 3),
            where_is_waldo(
                [["X", "X", "Y", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
            ),
        )


if __name__ == "__main__":
    unittest.main()