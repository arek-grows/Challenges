# https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python
# TODO: unfinished
import time
from math import sqrt


def remov_nb(n):
    end_list = []
    # find sum of all integers to n to check if prod(two numbers) == sum_to_n - prod(two numbers)
    sum_to_n = n * (n + 1) / 2
    n_sqrt = int(sqrt(n))
    # two for loops to iterate through all possible number combos up to n, without repeats
    count1 = 0
    for a in range(1, n):

        for b in range(a + 1, n + 1):
            count1 += 1
            prod = a * b
            sum_noab = sum_to_n - a - b
            # print(f"{a} * {b} = {prod} | sum_noab = {sum_noab}")
            if prod == sum_noab:
                end_list.append((a, b))
            if prod > sum_noab:
                print(f"broke at {a} {b}")
                break
    print(count1)
    return end_list


if __name__ == '__main__':
    tens = [10**xx for xx in range(1, 20)]
    for ii in [10]:
        start = time.time()
        print(remov_nb(ii))
        print(f"{ii}: {time.time() - start} seconds")


# 7000: 3.992300271987915 seconds
# init_prod = a * b, init_sum_noab = sum_to_n - a - b
# next: init_prod += b, init_sum_noab -= 1
