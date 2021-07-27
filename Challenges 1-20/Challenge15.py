# @Challenges #15 - Strictly Increasing or Decreasing

# Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.

# Examples
# check([1, 2, 3]) ➞ "increasing"

# check([3, 2, 1]) ➞ "decreasing"

# check([1, 2, 1]) ➞ "neither"

# check([1, 1, 2]) ➞ "neither"

# Notes

# - The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
# - Input lists have a minimum length of 2.


from typing import Sequence, AnyStr


def check(sequence: Sequence[int]) -> AnyStr:
    output = ""
    if sequence[0] < sequence[1]:
        output = "increasing"
    elif sequence[0] > sequence[1]:
        output = "decreasing"
    else:
        return "neither"

    x = len(sequence) - 1  # last index in the sequence
    i = 0  # current index being looked at (and+1)
    while i+1 != x:  # loop doesn't continue when current index is the last index
        i += 1
        if sequence[i] < sequence[i + 1] and output == "increasing":
            continue
        elif sequence[i] > sequence[i + 1] and output == "decreasing":
            continue
        else:
            return "neither"
    return output


assert check([1, 2, 3]) == "increasing"
assert check([3, 2, 1]) == "decreasing"
assert check([1, 2, 1]) == "neither"
assert check([1, 1, 2]) == "neither"
assert check([1, 3, 5, 7, 9, 10]) == "increasing"
assert check([5, 6, 5, 7, 9, 10]) == "neither"
assert check([5, 7]) == "increasing"
assert check([9, 7, 1]) == "decreasing"

#completed