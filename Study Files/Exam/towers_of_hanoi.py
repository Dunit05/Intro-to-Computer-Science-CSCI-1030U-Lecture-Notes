# Using the following function, towers_of_hanoi(), as a starting point, use operation counting (like you did in lab 09) to determine how many rings get moved (in terms of n), when calling towers_of_hanoi(n, 1, 2, 3).


# def towers_of_hanoi(n, start, end, temp):
#     if n < 1:
#         return

#     towers_of_hanoi(n - 1, start, temp, end)

#     print('Move 1 ring from', start, 'to', end) # count this line only

#     towers_of_hanoi(n - 1, temp, end, start)


# Note:  The operation being counted is how many times the print() statement is called.


# Note:  Do not use global variables to count these operations.  Use arguments and return values.


# The print statement is the only operation that you need to count.  Try various values for n (including 1, 2, 3, 4, 5, 6,7, and 8), and record the results in a comment inside the file.  Provide your best guess for an expression describing the performance of this algorithm (insertion_sort was n2, binary_search was log2n, for example), also in the comments for this function.


# An example comment (with the wrong values and guess) has been included below:


# '''
# best guess:  n^2
# n   prints
# ----------
# 1   2
# 2   5
# 3   10
# 4   17
# 5   26
# 6   37
# 7   50
# 8   65
# '''

# Hint: You can modify the function, including adding arguments and/or return values, in order to obtain the total count.


def towers_of_hanoi(n, start, end, temp):
    if n < 1:
        return 0

    op_count = towers_of_hanoi(n - 1, start, temp, end)

    print("Move 1 ring from", start, "to", end)  # count this line only
    op_count += 1

    op_count += towers_of_hanoi(n - 1, temp, end, start)

    return op_count


results = []
for n in range(1, 9):
    op_count = towers_of_hanoi(n, 0, 1, 2)
    results.append((n, op_count))
print(results)
