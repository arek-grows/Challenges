from typing import List
import unittest


def histogram(bars: List[int], char: str) -> str:
    end = []
    for x in bars:
        end.append(char * x)
    return "\n".join(end)  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("oo\noooo\nooooo\noooooo", histogram([2, 4, 5, 6], "o"))

    def test_2(self):
        self.assertEqual("****\n**", histogram([4, 2], "*"))

    def test_3(self):
        self.assertEqual(
            "HHHHHHHHHHHHHHHHHHHH\nH\nHHHHHHHHHHHH", histogram([20, 1, 12], "H")
        )

    def test_4(self):
        self.assertEqual(
            "##\n#\n##\n####\n#####\n##\n###", histogram([2, 1, 2, 4, 5, 2, 3], "#")
        )


if __name__ == "__main__":
    unittest.main()