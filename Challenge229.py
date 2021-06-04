# Challenge 229 - Sum Primes
#
# Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
# Examples
#
# sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
#
# sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
#
# sum_primes([]) ➞ None
#
# Notes
#
#     Given numbers won't exceed 101.
#     A prime number is a number which has exactly two divisors.


from __future__ import annotations
import unittest


def create_prime_list(up_to: int) -> list:
    prime_list = []
    is_prime = True
    for n in range(1, up_to + 1):
        if n <= 1:
            is_prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_list.append(n)
        is_prime = True
    return prime_list


def sum_primes(nums: list[int]) -> int:
    prime_list = create_prime_list(101)
    total = 0
    for num in nums:
        if num in prime_list:
            total += num
    if total == 0:
        return None
    return total  # Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 17)

    def test_2(self):
        self.assertEqual(sum_primes([2, 3, 4, 11, 20, 50, 71]), 87)

    def test_3(self):
        self.assertEqual(sum_primes([19, 21, 24, 27, 30, 37]), 56)

    def test_4(self):
        self.assertEqual(sum_primes([69, 79, 87, 97, 101]), 277)

    def test_5(self):
        self.assertEqual(sum_primes([53, 59, 28, 50, 45, 33, 61]), 173)

    def test_6(self):
        self.assertEqual(sum_primes([]), None)

    def test_7(self):
        self.assertEqual(sum_primes([11, 11, 11, 11, 11, 22, 22, 22]), 55)

    def test_8(self):
        self.assertEqual(sum_primes([67, 24, 58, 28, 71, 73, 99]), 211)


if __name__ == "__main__":
    unittest.main()