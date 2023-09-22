# Write some code that takes a list of floating point numbers, and prints the average of all of the numbers in the list

list = [1.4, 2.5, 3.6, 4.7, 5.8, 6.9, 7.0, 8.1, 9.2, 10.3]
sum = 0

for i in list:
    sum += i

print(sum / len(list))
