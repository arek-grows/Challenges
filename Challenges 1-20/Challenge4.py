# Create a function that takes numbers as arguments, adds them together, and returns the product of digits until the
# answer is only 1 digit long.


def sum_dig_prod(*args):
    total = str(sum(args))
    while len(total) > 1:
        total_list = []
        for number in total:
            total_list.append(int(number))
        total = total_list[0]
        i = 1
        for number in total_list[1:]:
            total = str(total * total_list[i])
    return int(total)


assert sum_dig_prod(16, 28) == 6
assert sum_dig_prod(0) == 0
assert sum_dig_prod(1, 2, 3, 4, 5, 6) == 2

# completed 5/26
