import unittest


def add_singles(numbers: int) -> int:
    numbers = str(numbers)
    numbers = list(numbers)
    end = 0
    for x in numbers:
        end += int(x)
    return end


def calculate_additive_persistence(number: int) -> int:
    end = add_singles(number)
    iterations = 1
    while end > 9:
        end = add_singles(end)
        iterations += 1
    return iterations  # Put your code here!!!


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, calculate_additive_persistence(13))

    def test_2(self):
        self.assertEqual(2, calculate_additive_persistence(1234))

    def test_3(self):
        self.assertEqual(2, calculate_additive_persistence(9876))

    def test_4(self):
        self.assertEqual(3, calculate_additive_persistence(199))


if __name__ == "__main__":
    unittest.main()