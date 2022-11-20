# not optimized for big numbers :(
# and yes I know, int() seems like the easy way, but it's not good for big numbers
def sum_strings(x, y):
    x = x[::-1]
    y = y[::-1]

    multiplier = 1
    x_int = 0
    for xx in x:
        x_int += int(xx) * multiplier
        multiplier *= 10

    multiplier = 1
    y_int = 0
    for yy in y:
        y_int += int(yy) * multiplier
        multiplier *= 10

    return str(x_int + y_int)


if __name__ == "__main__":
    print(sum_strings("123", "456"))
    print(sum_strings("123", "456") == "579")

    print(sum_strings("11111111", "11111111"))
