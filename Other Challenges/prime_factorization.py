# TODO: unfinished

from math import sqrt, floor
from random import randrange

# def finder(x):
#     print(f"x = {x}")
#     a = (x // 2)
#     b = (x * 4)
#     print(f"{b + 1} - {a * 2}")
#     return 1 + b - (a * 2)


def prime_facorization(num):
    prime_iterator = lambda x: 1 + (x * 4) - ((x // 2) * 2)
    max_q = floor(sqrt(num))
    p_iter = 1
    q = 2 if num % 2 == 0 else 3
    while q <= max_q and num % q != 0:
        q = prime_iterator(p_iter)
        p_iter += 1
    return [q] + prime_facorization(num // q) if q <= max_q else [num]


def factor_to_string(factors):
    factors_set = list(set(factors))
    factors_set.sort()
    end_string = ""
    for ff in factors_set:
        if factors.count(ff) == 1:
            end_string += f"({ff})"
        else:
            end_string += f"({ff}**{factors.count(ff)})"
    return end_string


if __name__ == '__main__':
    import time
    start_time = time.time()

    for xx in range(20):
        random_num = randrange(1, 1000000000000)
        factors = prime_facorization(random_num)
        print(f"{random_num}: {factor_to_string(factors)}")

    print(f"time: {time.time() - start_time}")
