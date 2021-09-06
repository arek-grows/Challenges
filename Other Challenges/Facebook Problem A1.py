# birthdays = int(input("Number of birthdays? "))
bday_strings = ["ABC", "F", "BANANA", "FBHC", "FOXEN", "CONSISTENCY"]
# for ii in range(1, birthdays + 1):
#     bday_strings.append(input(f"String {ii}? "))

case_results = []
vowels = ["A", "E", "I", "O", "U"]
for string in bday_strings:
    nr_con, nr_vow = 0, 0
    max_con, max_vow = 0, 0

    for ss in string:
        if ss in vowels:
            nr_vow += 1
            if (ss_count := string.count(ss)) > max_vow:
                max_vow = ss_count
        else:
            nr_con += 1
            if (ss_count := string.count(ss)) > max_con:
                max_con = ss_count

    replacements = (((nr_con - max_con) * 2 + nr_vow), ((nr_vow - max_vow) * 2 + nr_con))
    case_results.append(min(replacements))

for xx, rr in enumerate(case_results, start=1):
    print(f"Case #{xx}: {rr}")
