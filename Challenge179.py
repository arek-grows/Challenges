primes_up_to_97 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                    73, 79, 83, 89, 97)


def goldbachs_conjecture(number: int) -> list:
    primes = []
    set_list = []
    for prime in primes_up_to_97:  # create a list of primes that are less than 'number' for efficient looping l8r
        if prime >= number:
            break
        else:
            primes.append(prime)

    for a in primes:
        for b in primes:
            for c in primes:
                new_set = [a, b, c]
                new_set.sort()
                if a + b + c == number and new_set not in set_list:
                    set_list.append(new_set)
    return set_list


for n in range(7, 98, 2):
    print('%d: %s' %(n, str(goldbachs_conjecture(n))))