def consecutive_sum(n):
    max_possible = int(n / 2 + 1)
    for x in range(1, max_possible):
        total = 0
        for y in range(x, max_possible + 1):
            total += y
            if total == n:
                print(x, y)
                print(total)
                return True
            elif total > n:
                break
    return False


print(consecutive_sum(8))
