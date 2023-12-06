# Write a function (dc_find) that uses the divide and conquer algorithm strategy to find an element in an unsorted list.  The binary_search algorithm uses this same strategy on a sorted list, but searching an unsorted list.


# Recall that every divide and conquer algorithm uses the following steps to solve the problem:

# 1.      Divide the problem into something smaller (e.g. binary_search divides the list into two half lists)

# 2.      Conquer these sub-problems (recursively)

# 3.      Combine the solutions of these sub-problem


# Note:  Since the list isn't sorted, the value could be in the left half or the right half, so your algorithm will need to search both (unlike binary_search).


# Sample usage and output:

# if __name__ == '__main__':

#     print(f'dc_find([1,13,5,7,9,15], 8) == {dc_find([1,13,5,7,9,15], 8)}')

#     # output: dc_find([1,13,5,7,9,15], 8) == False


#     print(f'dc_find([1,13,5,7,9,15], 13) == {dc_find([1,13,5,7,9,15], 13)}')

#     # output: dc_find([1,13,5,7,9,15], 13) == True


def dc_find(elements, value):
    if len(elements) == 0:
        return False
    else:
        middle = len(elements) // 2
        if elements[middle] == value:
            return True
        else:
            return dc_find(elements[:middle], value) or dc_find(
                elements[middle + 1 :], value
            )


if __name__ == "__main__":
    print(f"dc_find([1,13,5,7,9,15], 8) == {dc_find([1,13,5,7,9,15], 8)}")
    # output: dc_find([1,13,5,7,9,15], 8) == False
    print(f"dc_find([1,13,5,7,9,15], 13) == {dc_find([1,13,5,7,9,15], 13)}")
    # output: dc_find([1,13,5,7,9,15], 13) == True
