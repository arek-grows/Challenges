# Challenge #19 - Generate N-Size Combinations
#
# Create a function that returns all combinations of size n from a list. Sort the list in ascending lexicographical
# order. Examples
#
# combo([1, 2, 3, 4], 1) ➞ [[1], [2], [3], [4]]
#
# combo([1, 2, 3, 4], 2) ➞ [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
#
# combo([1, 2, 3, 4], 5) ➞ []
#
# combo([1, 2, 3, 4], 0) ➞ [[]]
#
# Notes
#
# Lexicographical order: Compare the first element: [1, 2] will be before [2, 4]. If both share the same first
# element, compare the second element: [1, 2] is before [1, 3], etc. Return an empty list [] if n exceeds the length
# of the list. Return [[]] if n is 0 (see example #4). (Since there is only one combination of length 0: an empty
# list).


from typing import List


def combo(lst: List, size) -> List[List[int]]:
    combos = []
    if len(lst) < size:
        pass
    elif size == 0:
        combos.append([])
    else:
        for i in range(0, len(lst) - size + 1):
            current_combo = []
            for x in range(0, size):
                current_combo.append(lst[i])
            combos.append(current_combo)
    return combos  # Put your code here!


assert combo([1, 2, 3, 4], 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]  #  4 - 2 = 2 = the last index to work on
# +1. +2. +3. next +1. +2. next +1
assert combo([1, 2, 3, 4], 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]  #  len() - size = 1 (index)
# +1, +2. +1, +3. +2, +3. next for +1, +2.
assert combo([1, 2, 3, 4], 1) == [[1], [2], [3], [4]]  #  4 - 1 = 3 (index

assert combo([1, 2, 3, 4], 5) == []
assert combo([1, 2, 3, 4], 0) == [[]]
assert combo(['a', 'b', 'c'], 0) == [[]]
assert combo(['a', 'b', 'c'], 4) == []
assert combo(['a', 'b', 'c'], 1) == [['a'], ['b'], ['c']]
assert combo(['a', 'b', 'c'], 2) == [['a', 'b'], ['a', 'c'], ['b', 'c']]
assert combo(['a', 'b', 'c'], 3) == [['a', 'b', 'c']]
print("You successfully passed all Challenge 19 tests!!!")
