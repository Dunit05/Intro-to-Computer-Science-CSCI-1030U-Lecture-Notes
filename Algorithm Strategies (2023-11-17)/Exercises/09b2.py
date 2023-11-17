# Write a solution to the fractional knapsack problem in Python that uses the greedy strategy


def knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    for item in items:
        if capacity >= item[0]:
            capacity -= item[0]
            total_value += item[1]
        else:
            total_value += capacity * (item[1] / item[0])
            break
    return total_value


print(knapsack([(10, 60), (20, 100), (30, 120)], 50))
