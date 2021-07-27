import unittest


def is_followed_by_zeros(x):
    followed = str(x)
    followed = followed[1:]
    for x in followed:
        if x != '0':
            return False
    return True


def is_all_same(x):
    x = str(x)
    for o in range(1, len(x)):
        if o != x[0]:
            return False
    return True


# For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
# is there a way to do this better than i did?
def is_sequential_incrementing(x):
    x = str(x)
    # n_before is the first index of the number, which will be compared to the second in a for loop.
    # when loop ends, n_before is +1 which is compared to next index during next loop
    n_before = int(x[0])
    for n in x[1:]:
        n = int(n)
        if n_before == 9 and n == 0:
            pass
        elif n != n_before + 1:
            return False
        n_before += 1
    return True


# For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
def is_sequential_decrementing(x):
    x = str(x)
    n_before = int(x[0])
    for n in x[1:]:
        n = int(n)
        if n != n_before - 1:
            return False
        n_before -= 1
    return True


def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False


def is_interesting(mileage: int) -> int:
    # after the first loop, initial permanently turns into 1.
    # if a number turns out to be interesting, we add initial to interesting and return.
    initial = 2
    interesting = 0  # 0 not interesting, 1 will be interesting, 2 is interesting

    if mileage <= 99:
        return interesting  # a number is only interesting if it is greater than 99

    for x in range(3):  # current mileage + upcoming 2 miles
        if is_followed_by_zeros(mileage) or is_all_same(mileage) or is_sequential_incrementing(mileage) \
                or is_sequential_decrementing(mileage) or is_palindrome(mileage):
            return interesting + initial
        else:
            mileage += 1
            if initial == 2:
                initial = 1
    return interesting  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_interesting(3), 0)

    def test_2(self):
        self.assertEqual(is_interesting(11208), 0)

    def test_3(self):
        self.assertEqual(is_interesting(11209), 1)

    def test_4(self):
        self.assertEqual(is_interesting(11211), 2)

    def test_5(self):
        self.assertEqual(is_interesting(90000), 2)

    def test_6(self):
        self.assertEqual(is_interesting(89999), 1)

    def test_7(self):
        self.assertEqual(is_interesting(59998), 1)

    def test_8(self):
        self.assertEqual(is_interesting(59997), 0)

    def test_9(self):
        self.assertEqual(is_interesting(7890), 2)

    def test_10(self):
        self.assertEqual(is_interesting(7889), 1)

    def test_11(self):
        self.assertEqual(is_interesting(7888), 1)

    def test_12(self):
        self.assertEqual(is_interesting(1231), 0)

    def test_13(self):
        self.assertEqual(is_interesting(3210), 2)

    def test_14(self):
        self.assertEqual(is_interesting(12321), 2)

    def test_15(self):
        self.assertEqual(is_interesting(12320), 1)

    def test_16(self):
        self.assertEqual(is_interesting(12319), 1)

    def test_17(self):
        self.assertEqual(is_interesting(12318), 0)


if __name__ == "__main__":
    unittest.main()