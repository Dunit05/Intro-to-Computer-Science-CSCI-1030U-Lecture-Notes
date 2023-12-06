# Write a recursive function (get_powers_of_2) that takes an integer (n) and returns a list of the powers of 2 between 20 and 2n (inclusive).


# Sample usage:

# if __name__ == '__main__':

#     print(f'2^0 .. 2^4: {get_powers_of_2(4)}')

#     # output: [1, 2, 4, 8, 16]


#     print(f'2^0 .. 2^10: {get_powers_of_2(10)}')

#     # output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


def get_powers_of_2(n):
    if n == 0:
        return [1]
    else:
        return get_powers_of_2(n - 1) + [2**n]


if __name__ == "__main__":
    print(f"2^0 .. 2^4: {get_powers_of_2(4)}")
    # output: [1, 2, 4, 8, 16]
    print(f"2^0 .. 2^10: {get_powers_of_2(10)}")
    # output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
