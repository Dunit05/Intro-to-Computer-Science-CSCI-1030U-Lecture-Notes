# Write a function (sum_of_squares) that takes a minimum (min) and maximum (max) and returns the sum of the squares of all numbers between min and max (inclusive).


# Sample usage and output:

# if __name__ == '__main__':

#     print(f'sum_of_squares(1,10): {sum_of_squares(1,10)}')

#     # output: sum_of_squares(1,10): 385


#     print(f'sum_of_squares(1,5): {sum_of_squares(1,5)}')

#     # output: sum_of_squares(1,5): 55


def sum_of_squares(min, max):
    if min == max:
        return min**2
    else:
        return min**2 + sum_of_squares(min + 1, max)


if __name__ == "__main__":
    print(f"sum_of_squares(1,10): {sum_of_squares(1,10)}")
    # output: sum_of_squares(1,10): 385
    print(f"sum_of_squares(1,5): {sum_of_squares(1,5)}")
    # output: sum_of_squares(1,5): 55
