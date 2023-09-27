# Write a program that, given a list of values and a list of names, generates a dictionary containing the same data
# The order of the elements should be in the same order in each list

values = [1, 2, 3, 4, 5]
names = ["one", "two", "three", "four", "five"]
dictionary = {}

for i in range(len(values)):
    dictionary[names[i]] = values[i]

print(dictionary)
