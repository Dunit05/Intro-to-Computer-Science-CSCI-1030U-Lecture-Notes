# Write a program that asks the user for two numbers, and outputs the modulus of 5 of the sum of those two numbers

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

calculated_number = (first_number + second_number) % 5

print("The remainder is", calculated_number)
