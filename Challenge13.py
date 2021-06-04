# A consecutive-run is a list of adjacent, consecutive integers. Create a function that takes a list of numbers and
# returns the length of the longest consecutive-run.
#
# To illustrate:
#
# longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# # Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
#
# longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
# # Longest consecutive-run: [1, 2, 3].
#
# longest_run([3, 5, 7, 10, 15]) ➞ 1
# # No consecutive runs, so we return 1.
#
# Notes
#
# If there aren't any consecutive runs (there is a gap between each integer), return 1.
from typing import Sequence


def longest_run(numbers: Sequence[int]) -> int:
    longest_sequence = 1
    current_sequence = 1
    pos = False
    neg = False

    def is_longest_sequence(now, longest):
        if now > longest:
            return now
        return longest

    i = 0
    while i < len(numbers) - 1:
        if numbers[i] + 1 == numbers[i+1]:
            pos = True
            current_sequence += 1
        elif numbers[i] - 1 == numbers[i+1]:
            neg = True
            current_sequence += 1
        else:
            current_sequence = 1
        i += 1
        longest_sequence = is_longest_sequence(current_sequence, longest_sequence)
        while pos and i < len(numbers) - 1:
            if numbers[i] + 1 == numbers[i+1]:
                current_sequence += 1
            else:
                pos = False
                current_sequence = 1
            longest_sequence = is_longest_sequence(current_sequence, longest_sequence)
            i += 1
        while neg and i < len(numbers) - 1:
            if numbers[i] - 1 == numbers[i+1]:
                current_sequence += 1
            else:
                neg = False
                current_sequence = 1
            longest_sequence = is_longest_sequence(current_sequence, longest_sequence)
            i += 1
    return longest_sequence


assert longest_run([1, 2, 3, 5, 6, 7, 8, 9]) == 5
assert longest_run([1, 2, 3, 10, 11, 15]) == 3
assert longest_run([-7, -6, -5, -4, -3, -2, -1]) == 7
assert longest_run([3, 5, 6, 10, 15]) == 2
assert longest_run([3, 5, 7, 10, 15]) == 1
print("Challenge #13 - Longest Run - Successfully Ran")

# completed 6/9
