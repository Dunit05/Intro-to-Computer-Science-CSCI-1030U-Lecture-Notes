# Write a function (are_equal) that takes two lists (list1, list2), and returns True if every value from list1 is in list2, and vice versa (order ignored) (for the math inclined, this is similar to set equality).

# Note: Do not consider duplicates in this example.  You may assume that neither list contains any duplicated items.

# Sample usage:

# if __name__ == '__main__':

#     print(f'are_equal([1,2,3], [3,1,2]): {are_equal([1,2,3], [3,1,2])}')

#     # are_equal([1,2,3], [3,1,2]): True


#     print(f'are_equal([1,2,3], [4,1,3]): {are_equal([1,2,3], [4,1,3])}')

#     # are_equal([1,2,3], [4,1,3]): False


#     print(f'are_equal([1,8,15], [1,15,8]): {are_equal([1,8,15], [1,15,8])}')

#     # are_equal([1,8,15], [1,15,8]): True


def are_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for item in list1:
            if item not in list2:
                return False
        return True


if __name__ == "__main__":
    print(f"are_equal([1,2,3], [3,1,2]): {are_equal([1,2,3], [3,1,2])}")
    # are_equal([1,2,3], [3,1,2]): True
    print(f"are_equal([1,2,3], [4,1,3]): {are_equal([1,2,3], [4,1,3])}")
    # are_equal([1,2,3], [4,1,3]): False
    print(f"are_equal([1,8,15], [1,15,8]): {are_equal([1,8,15], [1,15,8])}")
    # are_equal([1,8,15], [1,15,8]): True
