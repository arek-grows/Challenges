hamming_number_list = []


def is_hamming_number(num):
    if num in hamming_number_list:
        return True
    if num == 1:
        hamming_number_list.append(num)
        return True
    if num % 2 == 0:
        return is_hamming_number(num / 2)
    if num % 3 == 0:
        return is_hamming_number(num / 3)
    if num % 5 == 0:
        return is_hamming_number(num / 5)
    return False


counter = 0
for xx in range(1, 1_000_000_000):
    if is_hamming_number(xx):
        counter += 1
        print(f"{counter}: {xx}")