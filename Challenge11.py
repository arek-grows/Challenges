# A Collatz sequence is generated like this.
#
#     Start with a positive number
#     If it's even, halve it
#     If it's odd, multiply it by 3 and add one
#     Repeat the process with the resulting number
#
# The Collatz Conjecture is that every sequence eventually reaches 1 (continuing past 1 just results in an endless
# repeat of the sequence (4, 2, 1)).
#
# The length of the sequence from starting number to 1 varies widely.
#
# Create a function that takes a number as an argument and returns the number of steps in the Collatz sequence it
# took to reach 1.


def collatz(number):
    sequence_length = 1
    while number != 1:
        sequence_length += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
    return sequence_length


assert collatz(3) == 8
assert collatz(7) == 17
assert collatz(17) == 13
assert collatz(42) == 9
assert collatz(33) == 27
print("Success, all tests passed!")