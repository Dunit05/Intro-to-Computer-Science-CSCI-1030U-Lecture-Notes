# Write a recursive function (filter_primes) that takes a list (elements) and returns a list that contains the elements from elements that were prime numbers.  You can write a non-recursive function (is_prime) to determine if a single number of a prime, returning a Boolean result.


# Sample usage and output:

# if __name__ == '__main__':

#     print(f'filter_primes(range(20)): {filter_primes(range(20))}')

#     # output:  filter_primes(range(20)): [1, 2, 3, 4, 5, 7, 11, 13, 17, 19]


#     print(f'filter_primes(range(100,200)): {filter_primes(range(100,200))}')

#     # output:  filter_primes(range(100,200)): [101, 103, 107, 109, 113, 127,

#     #          131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,

#     #          193, 197, 199]


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def filter_primes(elements):
    primes = []
    for element in elements:
        if is_prime(element):
            primes.append(element)
    return primes


if __name__ == "__main__":
    print(f"filter_primes(range(20)): {filter_primes(range(20))}")
    # output:  filter_primes(range(20)): [1, 2, 3, 4, 5, 7, 11, 13, 17, 19]
    print(f"filter_primes(range(100,200)): {filter_primes(range(100,200))}")
    # output:  filter_primes(range(100,200)): [101, 103, 107, 109, 113, 127,
    #          131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
    #          193, 197, 199]
