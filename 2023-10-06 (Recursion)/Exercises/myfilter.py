# Write your own recursive version of the filter function, called myfilter, which:
# Takes a unary function (check) and a list (values) as arguments
# Applies the function check to successive each value from the list, and if the result is True, adds the value to the output list
# For example:


# marks = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
# a_grades = myfilter(lambda mark: mark > 80.0, marks)
# a_grades should be [87.0, 94.0, 100.0]


def myfilter(check, values):
    if len(values) == 0:
        return []
    else:
        if check(values[0]):
            return [values[0]] + myfilter(check, values[1:])
        else:
            return myfilter(check, values[1:])


marks = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
a_grades = myfilter(lambda mark: mark > 80.0, marks)
print(a_grades)
