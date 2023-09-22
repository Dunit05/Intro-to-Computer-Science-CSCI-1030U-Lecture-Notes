# Write some code that takes a list of floating point numbers, and prints the average of all of the even numbers in the list

list = [3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0, 10.1, 11.2, 12.3]
sum = 0

for i in list:
    if i % 2 == 0:
        sum += i

print(sum / len(list))
