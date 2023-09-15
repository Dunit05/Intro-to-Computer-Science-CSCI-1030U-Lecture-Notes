# Write a program that asks the user for two numbers, and outputs the message Both numbers are even only if both numbers are even

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")
else:
    print("Both numbers are not even")
