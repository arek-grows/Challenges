# Create a function that takes in a list and returns a list of the accumulating sum. So each number in the list
# should be summed with all numbers before it in the list.
#
# [1, 2, 3]
# 1 no numbers before it so add 1 to the output list
# 2, 1 is before it so add them together and put the result of 3 in the output list
# 3, 1 & 2 are before it so sum all 3 together and put the result of 6 in the output list
# Output will be [1, 3, 6]


def accumulating_list_bad(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers
    end_list = [numbers[0], numbers[0] + numbers[1]]
    i = 2
    for number in numbers[i:]:
        end_list.append(end_list[i-1]+numbers[i])
        i += 1
    return end_list

# BETTER:


def accumulating_list(numbers):
    i = 0
    end_list = []
    for number in numbers:
        i = i + number
        end_list.append(i)
    return end_list


assert accumulating_list([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
assert accumulating_list([1, 5, 7]) == [1, 6, 13]
assert accumulating_list([1, 0, 1, 0, 1]) == [1, 1, 2, 2, 3]
assert accumulating_list([1, 2, 3, 0, 0, 1]) == [1, 3, 6, 6, 6, 7]
assert accumulating_list([]) == []

# complete 5/25
