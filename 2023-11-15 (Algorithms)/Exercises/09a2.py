# Let's use operation counting to estimate the performance of the following algorithm
# The operations to be counted are the number of comparisons made
# Try collecting data for lists of size 10, 100, 1000, and 10000


def sequential_search(values, to_find):
    num_comps = 0
    for i in range(len(values)):
        num_comps += 1
        if values[i] == to_find:
            return True, num_comps
    return False, num_comps


print(sequential_search([1, 2, 3, 4, 5], 3))
