## -
# # Challenge #20 - Groceries
#
# # Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it
# as a number. A grocery dictionary has a product, a quantity and a price, for example:
#
# # {
#   # "product": "Milk",
#   # "quantity": 1,
#   # "price": 1.50
# # }
#
# # Examples
#
# 1 bottle of milk:
# # get_total_price([
#   # { "product": "Milk", "quantity": 1, "price": 1.50 }
# # ]) ➞ 1.5
#
# 1 bottle of milk & 1 box of cereals:
# # get_total_price([
#   # { "product": "Milk", "quantity": 1, "price": 1.50 },
#   # { "product": "Cereals", "quantity": 1, "price": 2.50 }
# # ]) ➞ 4
#
# 3 bottles of milk:
# # get_total_price([
#   # { "product": "Milk", "quantity": 3, "price": 1.50 }
# # ]) ➞ 4.5
#
# Several groceries:
# # get_total_price([
#   # { "product": "Milk", "quantity": 1, "price": 1.50 },
#   # { "product": "Eggs", "quantity": 12, "price": 0.10 },
#   # { "product": "Bread", "quantity": 2, "price": 1.60 },
#   # { "product": "Cheese", "quantity": 1, "price": 4.50 }
# # ]) ➞ 10.4
#
# Some cheap candy:
# # get_total_price([
#   # { "product": "Chocolate", "quantity": 1, "price": 0.10 },
#   # { "product": "Lollipop", "quantity": 1, "price": 0.20 }
# # ]) ➞ 0.3
#
# # Notes
#
# # There might be a floating point precision problem in here...


from typing import Dict, List
from decimal import Decimal


def get_total_price(groceries: List[Dict]) -> int:
    total_price = 0
    for grocery in groceries:
        total_price += grocery['quantity'] * grocery['price']
        total_price = round(total_price, 2)
        print(total_price)
    return total_price


assert get_total_price([
    {"product": "Milk", "quantity": 1, "price": 1.50}
]) == 1.5

assert get_total_price([
    {"product": "Milk", "quantity": 1, "price": 1.50},
    {"product": "Cereals", "quantity": 1, "price": 2.50}
]) == 4

assert get_total_price([
    {"product": "Milk", "quantity": 3, "price": 1.50}
]) == 4.5

assert get_total_price([
    {"product": "Milk", "quantity": 1, "price": 1.50},
    {"product": "Eggs", "quantity": 12, "price": 0.10},
    {"product": "Bread", "quantity": 2, "price": 1.60},
    {"product": "Cheese", "quantity": 1, "price": 4.50}
]) == 10.4

assert get_total_price([
    {"product": "Chocolate", "quantity": 1, "price": 0.10},
    {"product": "Lollipop", "quantity": 1, "price": 0.20}
]) == 0.3
print("You successfully passed all Challenge 20 tests!!!")
