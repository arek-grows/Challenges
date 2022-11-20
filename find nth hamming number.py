# TODO: 30 calculates incorrectly bc you're multiplying two numbers rather than three (line 27)

def find_if_ham(num):
    # inneficient way. this might be better to find i, j, k of 2^i 3^j 5^k
    power_dict = {2: [], 3: [], 5: []}

    for power in power_dict:

        current_power = 1

        while True:

            current_powered = power ** current_power

            if current_powered == num:
                return True
            elif current_powered < num:
                power_dict[power].append(current_powered)
                current_power += 1
            else:
                break

    powers = tuple(power_dict[2] + power_dict[3] + power_dict[5])
    # print(powers)
    for ii, aa in enumerate(powers[:-1]):
        for bb in powers[ii + 1:]:
            if aa * bb == num:
                return True

    return False

    # prime factorization approach. still not fast enough
    # ii = 2
    # while ii <= num:
    #     if num % ii == 0:
    #         num /= ii
    #     else:
    #         ii += 1
    #         if ii > 5:
    #             return False
    # return True


def hamming(n):
    """Returns the nth hamming number"""
    if n == 1:
        return 1

    current_num = 2
    ham_nums_found = 1

    while True:
        # print(f"Looking at {current_num}:")
        if find_if_ham(current_num):
            # print(f"Hamming number {ham_nums_found + 1} is {current_num}.")
            ham_nums_found += 1

        if ham_nums_found == n:
            return current_num
        else:
            # print(f"False.")
            current_num += 1


if __name__ == "__main__":
    counter = 0
    for xx in range(1, 33):
        counter += 1
        print(f"Hamming {counter} is {hamming(xx)}")
