# Write a search algorithm in Python that uses the divide and conquer strategy, but doesn't require that the list be sorted


def search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return search(list[midpoint + 1 :], target)
            else:
                return search(list[:midpoint], target)


print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
