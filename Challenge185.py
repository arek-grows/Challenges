import unittest


def sequence(steps: int) -> int:
    output = 0
    step_one = True
    for x in range(steps):
        if step_one:
            output += 3
            step_one = False
        else:
            output -= 1
            step_one = True
    return output  # Put your code here!!!

# for a more efficient function, i could have used the modular operator to do every step at once


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sequence(5), 7)

    def test_2(self):
        self.assertEqual(sequence(0), 0)

    def test_3(self):
        self.assertEqual(sequence(6), 6)

    def test_4(self):
        self.assertEqual(sequence(99), 101)

    def test_5(self):
        self.assertEqual(sequence(2), 2)

    def test_6(self):
        self.assertEqual(sequence(1), 3)


if __name__ == "__main__":
    unittest.main()
