# Tommy D. Michailidis
# 2023-11-03
# Computer Science Mid Term #2


def math3(x, n=1, max_n=10):
    if n > max_n:
        return 0
    else:
        return 2 * ((x**n) / n) + math3(x, n + 2, max_n)


# ! For Testing Only
print(f"{math3(0.0, n = 1, max_n = 10) = }")
# output: math3(0.0, n = 1, max_n = 10) = 0.0

print(f"{math3(0.5, n = 1, max_n = 10) = }")
# output: math3(0.5, n = 1, max_n = 10) = 1.0986120290116657
