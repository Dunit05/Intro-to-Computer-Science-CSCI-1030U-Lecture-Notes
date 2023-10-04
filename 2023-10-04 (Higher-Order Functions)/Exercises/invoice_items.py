# Using the reduce function, take a list of dictionaries called invoice_items, and computes the total cost:
# Each dictionary in invoice_items has a field named item_price, and another field named quantity
# The total cost for each item is item_price * quantity
# The function that you pass to reduce will obtain these two quantities, and add their product to the sum
# Try it with a lambda function, if you can

from functools import reduce

invoice_items = [
    {"Item": "item1", "item_price": 1.99, "quantity": 2},
    {"Item": "item2", "item_price": 2.99, "quantity": 3},
    {"Item": "item3", "item_price": 3.99, "quantity": 4},
]

total_cost = reduce(lambda x, y: x + y["item_price"] * y["quantity"], invoice_items, 0)

# Round to 2 decimal places
total_cost = round(total_cost, 2)

print(total_cost)
