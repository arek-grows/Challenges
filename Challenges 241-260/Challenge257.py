import unittest


primes_list = []  # primes up to 3,500

for possible_prime in range(2, 3500):
    is_prime = True
    for num in range(2, possible_prime):
        if possible_prime % num == 0:
            is_prime = False
            break
    if is_prime:
        primes_list.append(possible_prime)


def primal_strength(prime: int) -> str:
    over_difference = primes_list[primes_list.index(prime) + 1] - prime
    under_difference = prime - primes_list[primes_list.index(prime) - 1]
    if over_difference == under_difference:
        return "Balanced"
    elif over_difference < under_difference:
        return "Strong"
    else:
        return "Weak"
# Put your code here!!!


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(primal_strength(5), "Balanced")

    def test_2(self):
        self.assertEqual(primal_strength(211), "Balanced")

    def test_3(self):
        self.assertEqual(primal_strength(593), "Balanced")

    def test_4(self):
        self.assertEqual(primal_strength(1693), "Strong")

    def test_5(self):
        self.assertEqual(primal_strength(599), "Strong")

    def test_6(self):
        self.assertEqual(primal_strength(2203), "Strong")

    def test_7(self):
        self.assertEqual(primal_strength(19), "Weak")

    def test_8(self):
        self.assertEqual(primal_strength(2971), "Weak")

    def test_9(self):
        self.assertEqual(primal_strength(1493), "Weak")


if __name__ == "__main__":
    unittest.main()