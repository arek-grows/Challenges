# https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python
import time
from math import sqrt


def remov_nb(n):
    end_list = []
    # find sum of all integers to n to check if prod(two numbers) == sum_to_n - a - b
    sum_to_n = n * (n + 1) / 2
    for a in range(1, n + 1):
        # equation for finding b, given a and sum of all integers to n
        # a * b == sum_to_n - a - b
        # (a + 1) * b == sum_to_n - a
        # b == (sum_to_n - a) / (a + 1)
        b = (sum_to_n - a) / (a + 1)
        # if b is an integer and within n, append (a, b)
        if b.is_integer() and b <= n:
            end_list.append((a, int(b)))
    return end_list


if __name__ == '__main__':
    tens = [10**xx for xx in range(1, 20)]
    for ii in range(4, 10001):
        start = time.time()
        rnbs = remov_nb(ii)
        if len(rnbs) > 6:
            print(f"{ii}: {rnbs}")
        # print(f"{ii}: {time.time() - start} seconds")
