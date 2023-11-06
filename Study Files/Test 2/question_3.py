# Tommy D. Michailidis
# 2023-11-03
# Computer Science Mid Term #2


def higher_order2(values, op):
    return max(values, key=op)


# ! For Testing Only
def times_two(x):
    return x * 2


print(f"{higher_order2([2,1,3], times_two) = }")
# output: higher_order2([2,1,3], times_two) = 3

print(f"{higher_order2([-6,3,2], lambda x: x ** 2) = }")
# output: higher_order2([-6,3,2], lambda x: x ** 2) = -6
