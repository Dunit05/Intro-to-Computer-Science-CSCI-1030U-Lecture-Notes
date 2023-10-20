print("Question 1:")
n = 4


def drawSquare(n):
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print("")


drawSquare(n)

print("Question 2:")
n = 4


def drawTriangle(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("*", end="")
        print("")


drawTriangle(n)

print("Question 3:")
n = 4


def drawTriangle2(n):
    for row in range(1, n + 1):
        for col in range(1, row):
            print(" ", end="")
        for col in range(row, n + 1):
            print("*", end="")
        print("")


drawTriangle2(n)

print("Question 4:")
list = [5, 8, 3, 21, 7, 4, 14]


def jumpMaximum(list):
    maxVal = list[0]
    maxPos = 0

    for i in range(1, len(list)):
        if maxVal < list[i]:
            maxVal = list[i]
            maxPos = i

    firstVal = list[0]
    list[0] = maxVal
    list[maxPos] = firstVal

    return list


print(jumpMaximum(list))

print("Question 5:")
list = [5, 8, 3, 21, 7, 4, 14]


def doubleList(list):
    for i in range(0, len(list)):
        list[i] = list[i] * 2
    return list


print(doubleList(list))

print("Question 6:")
list = [5, 8, 3, 21, 7, 4, 14]
min = 4
max = 14


def sublistInRange(list, min, max):
    newList = []
    for elem in list:
        if elem >= min and elem <= max:
            newList.append(elem)

    return newList


print(sublistInRange(list, min, max))

print("Question 7:")


def drawParallelogram(n):
    spaces = 0
    for line in range(n):
        print(" " * spaces, end="")
        print("*" * n)
        spaces += 1


drawParallelogram(7)
drawParallelogram(5)

print("Question 8:")


def countLessThan(list, max):
    count = 0
    for elem in list:
        if elem < max:
            count = count + 1
    return count


list = [7, 21, 4, 19, 6, 31, 16, 20, 11]

print("how many values in", list, "<", 7, "?", countLessThan(list, 7))
# 2
print("how many values in", list, "<", 20, "?", countLessThan(list, 20))
# 6
print("how many values in", list, "<", 2, "?", countLessThan(list, 2))
# 0

print("Question 9:")


def isReordering(list1, list2):
    for elem in list1:
        if elem not in list2:
            return False
    return len(list1) == len(list2)


def isReordering_easy_version(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2


print("isReordering([4,1,3,2],[1,2,3,4]):", isReordering([4, 1, 3, 2], [1, 2, 3, 4]))
# True
print("isReordering([5,8,3,21],[5,21,8]):", isReordering([5, 8, 3, 21], [5, 21, 8]))
# False

print("Question 10:")


def isReverse(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        j = len(word1) - i - 1
        if word1[i] != word2[j]:
            return False
    return True


print("isReverse([4,3,2,1],[1,2,3,4]):", isReverse([4, 3, 2, 1], [1, 2, 3, 4]))
# True
print("isReverse([4,1,3,2],[1,2,3,4]):", isReverse([4, 1, 3, 2], [1, 2, 3, 4]))
# False
