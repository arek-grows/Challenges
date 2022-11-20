def create_singular_duration_string(time, time_type):
    if time > 1:
        time_type += "s"
    return f"{time} {time_type}"


def create_format_duration_string(duration_list):
    if len(duration_list) == 1:
        return f"{duration_list[0]}"
    if len(duration_list) == 2:
        return f"{duration_list[0]} and {duration_list[1]}"
    if len(duration_list) >= 3:
        beginning = ""
        for dd in duration_list[:-2]:
            beginning += f"{dd}, "
        return f"{beginning}{duration_list[-2]} and {duration_list[-1]}"
    return "now"


def format_duration(seconds):
    duration_string_list = []
    seconds_dict = {"year": 31_536_000, "day": 86400, "hour": 3600, "minute": 60}

    for time_type, seconds_amount in seconds_dict.items():
        if seconds >= seconds_amount:
            duration_string_list.append(create_singular_duration_string(seconds // seconds_amount, time_type))
            seconds %= seconds_amount

    if seconds <= 59 and seconds != 0:
        duration_string_list.append(create_singular_duration_string(seconds, "second"))
        return create_format_duration_string(duration_string_list)

    return create_format_duration_string(duration_string_list)


if __name__ == "__main__":
    print(format_duration(3662))
    print(format_duration(3662) == "1 hour, 1 minute and 2 seconds")

    print(f"9,546,738,219 seconds is equal to {format_duration(9546738219)}")
