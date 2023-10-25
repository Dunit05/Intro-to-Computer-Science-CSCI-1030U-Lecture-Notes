# Tommy D. Michailidis
# #100911141, Midterm 1


# Function min_of_divisible_by_3(numbers)
def min_of_divisible_by_3(numbers):
    # Create & Initialize a new temp List
    newlist = []
    # Iterate though each number
    for number in numbers:
        # if the number is divisible by 3
        if number % 3 == 0:
            # add the number to the list
            newlist.append(number)
    # return the minimum number in the new list
    return min(newlist)


# ! Testing
print(min_of_divisible_by_3([21, 3, 12, 8, 35, 9, 18, 10, 1, 15, 19, 5, 25]))
print(min_of_divisible_by_3([7, 11, 12, 4, 1, 10, 9, 2, 6]))
