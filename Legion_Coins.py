import matplotlib.pyplot as plt

levels = range(60, 301)
level_mod = {99: 0.5, 139: 0.4, 179: 0.7, 199: 0.8, 209: 1,
             219: 1.1, 229: 1.15, 239: 1.2, 249: 1.25, 259: 1.3,
             269: 1.35, 279: 1.4, 289: 1.45, 299: 1.5, 300: 1.55}
coin_per_day = []


for ll in levels:
    mod = 0
    for level in level_mod:
        if ll <= level:
            mod = level_mod[level]
            break
    combat_power = mod * pow(ll, 3)
    coin_per_day.append(combat_power/1251251.26)

fig, ax = plt.subplots()
ax.plot(levels, coin_per_day)
plt.show()
