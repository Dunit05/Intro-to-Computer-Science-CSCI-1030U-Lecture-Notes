# Write a program that asks the user for a single mark (out of 100), and outputs the letter grade that corresponds to that mark
# Use the following ranges:
# 0-49: 	F
# 50-59: 	D
# 60-69: 	C
# 70-79: 	B
# 80-100: A

mark = int(input("Enter a mark: "))

# print(
#     "A"
#     if mark >= 80
#     else "B"
#     if mark >= 70
#     else "C"
#     if mark >= 60
#     else "D"
#     if mark >= 50
#     else "F"
# )

if mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("F")
