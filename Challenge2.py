# Given the month and year as numbers, return whether that month contains a Friday 13th.


import datetime


def has_friday_13(month, year):
    x = datetime.datetime(year, month, 13)
    if x.strftime("%A") == "Friday":
        return True
    return False


assert has_friday_13(3, 2020) == True
assert has_friday_13(10, 2017) == True
assert has_friday_13(1, 1985) == False
print("Success")

# completed 5/26
