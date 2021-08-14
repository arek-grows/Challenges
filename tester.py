import random

letters = ["s", "a", "d", "f", "g", "h"]
l_dict = {}

for letter in letters:
    l_dict[letter] = random.randint(0, 100)

sorted_dict = [(v, k) for k, v in l_dict.items()]

[print(a[1]) for a in sorted_dict]

print("{:b}".format(100).count("1"))