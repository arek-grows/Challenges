names =             [
                "Heather Mcgee",
                "Nicole Yoder",
                "Melissa Hoffman",
                "Jennifer Figueroa",
                "Amanda Schwartz",
            ]

last_lengths = []
for name in names:
    name = name.split()
    last_lengths.append( [len(name[1])] + name)
    last_lengths.sort()

print(last_lengths)

listwer = [] * 4
print(listwer)