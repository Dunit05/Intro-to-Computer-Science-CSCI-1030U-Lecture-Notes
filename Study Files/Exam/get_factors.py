# Write a function (get_factors) that takes an integer (n) and returns a list of all of the integer factors of n.


# Sample usage and output:

# if __name__ == '__main__':

#     print(f'Factors of 12: {get_factors(12)}')

#     # output: Factors of 12: [1, 2, 3, 4, 6, 12]


#     print(f'Factors of 20: {get_factors(20)}')

#     # output: Factors of 20: [1, 2, 4, 5, 10, 20]


#     print(f'Factors of 100: {get_factors(100)}')

#     # output: [1, 2, 4, 5, 10, 20, 25, 50, 100]


def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


if __name__ == "__main__":
    print(f"Factors of 12: {get_factors(12)}")
    # output: Factors of 12: [1, 2, 3, 4, 6, 12]
    print(f"Factors of 20: {get_factors(20)}")
    # output: Factors of 20: [1, 2, 4, 5, 10, 20]
    print(f"Factors of 100: {get_factors(100)}")
    # output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
