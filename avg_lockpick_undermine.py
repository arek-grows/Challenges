import random


def lockpick_sim():
    used = 1
    for i in range(2, 100, 2):
        used += 1
        if random.randint(1, 100) <= i:
            return used


uses = []
num_sims = 10000000
for sim in range(num_sims):
    uses.append(lockpick_sim())

pad_size = 2
for x in range(2, max(uses)):
    num = str(x).rjust(pad_size)
    percent = '{0:.2g}'.format(uses.count(x) / num_sims * 100)
    print(f"{num} | {percent}%")
