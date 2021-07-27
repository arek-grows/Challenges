# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You
# are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
# and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the
# inventory has been sold.


def profit(data):
    return round((data["sell_price"] - data["cost_price"]) * data["inventory"])


assert profit({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}) == 14796
assert profit({"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}) == 32411
assert profit({"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}) == 44030
assert profit({"cost_price": 2.25, "sell_price": 5.0, "inventory": 1}) == 3  # Edge case for testing rounding
print("Success")
