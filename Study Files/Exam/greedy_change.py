# Write a function (greedy_change) that uses the greedy algorithm strategy to give proper change for any denominations of currency.  For simplicity, you can assume that the amounts are all integers (so you won't have to deal with floating point errors.  The greedy_change function will take two arguments:

# ·        amount - this is the total amount of change to be returned to the customer

# ·        denoms - a list of (integer) currency values, i.e. denominations, not necessarily in any order


# Recall that every greedy algorithm repeatedly makes the immediately greedy choice.  This means different things for different problems, but in this case, it means that you want to give the largest amount of change possible each time, so that you minimize the number of bills required.  As such, you will want to sort the list of denominations (in decreasing order) so that you can consider the largest currency denominations before the smaller ones.


# To sort a list in descending order, you can use the built-in sort() function:


# denoms.sort(reverse=True)


# Sample usage and output:

# if __name__ == '__main__':

#     denoms = [1,2,5,10,20,50]


#     print(f'greedy_change(174, {denoms}) == {greedy_change(174, denoms)}')

#     # output: greedy_change(174, [1,2,5,10,20,50]) == [50, 50, 50, 20, 2, 2]


#     print(f'greedy_change(99, {denoms}) == {greedy_change(99, denoms)}')

#     # output: greedy_change(99, [1,2,5,10,20,50]) == [50, 20, 20, 5, 2, 2]


def greedy_change(amount, denoms):
    denoms.sort(reverse=True)
    change = []
    for denom in denoms:
        while amount >= denom:
            change.append(denom)
            amount -= denom
    return change


if __name__ == "__main__":
    denoms = [1, 2, 5, 10, 20, 50]
    print(f"greedy_change(174, {denoms}) == {greedy_change(174, denoms)}")
    # output: greedy_change(174, [1,2,5,10,20,50]) == [50, 50, 50, 20, 2, 2]
    print(f"greedy_change(99, {denoms}) == {greedy_change(99, denoms)}")
    # output: greedy_change(99, [1,2,5,10,20,50]) == [50, 20, 20, 5, 2, 2]
