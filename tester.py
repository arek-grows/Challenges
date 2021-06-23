import random

random_list = []
for x in range(100000):
    random_number = random.randrange(1, 5)  # or whatever random function you're using
    random_list.append(random_number)
for n in range(1, 5):  # same as the range used for random number generation
    print("distribution of %s: %f" % (n, (random_list.count(n) / 1000)))
