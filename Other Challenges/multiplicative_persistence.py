def persist(n, steps=0, show_work=False):
    n_string = str(n)
    if show_work is True:
        print(n_string)
    if len(n_string) == 1:
        return steps
    else:
        steps += 1
        total = 1
        for nn in n_string:
            total *= int(nn)
        return persist(total, steps, show_work)


record = [0, 0]  # record and record-breaker
for ii in range(277777788888899 + 1):
    nr_steps = persist(ii)
    if nr_steps > record[0]:
        record[0] = nr_steps
        record[1] = ii
        print(record)

print(record)
persist(record[1], 0, True)
