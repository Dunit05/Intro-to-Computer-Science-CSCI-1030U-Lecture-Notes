# Tommy D. Michailidis
# 2023-12-06
# Final Exam


def max_dc(values):
    if len(values) == 0:
        return False
    elif len(values) == 1:
        return values[0]

    middle = len(values) // 2
    max_left = max_dc(values[:middle])
    max_right = max_dc(values[middle:])
    return max_left if max_left > max_right else max_right


print(f"{max_dc([106,5,-3,17,-21,39]) = }")
print(f"{max_dc([-106,5,-3,17,-21,39]) = }")
print(f"{max_dc([-106,5,-3,17,21,-39]) = }")
