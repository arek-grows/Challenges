def solution(args):
    previous_num = args[0]
    range_list = []
    end_list = []

    if len(args) == 1:
        return f"{str(previous_num)}"

    if args[0] + 1 == args[1]:
        range_list.append(args[0])
    else:
        end_list.append(str(args[0]))

    for num in args[1:]:
        if previous_num + 1 == num:
            range_list.append(num)
        elif len(range_list) > 2:
            end_list.append(f"{range_list[0]}-{range_list[-1]}")
            range_list.clear()
            range_list.append(num)
        elif len(range_list) <= 2:
            for nn in range_list:
                end_list.append(str(nn))
            range_list.clear()
            range_list.append(num)
        previous_num = num
    if len(range_list) <= 2:
        for nn in range_list:
            end_list.append(str(nn))
    elif len(range_list) > 2:
        end_list.append(f"{range_list[0]}-{range_list[-1]}")

    return ",".join(end_list)


if __name__ == "__main__":
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) == '-3--1,2,10,15,16,18-20')
    print(solution(
        [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == '-6,-3-1,3-5,7-11,14,15,17-20')

    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
