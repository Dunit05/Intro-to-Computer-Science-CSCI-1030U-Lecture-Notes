# Write some code to output 1/n for all n in the list [5,4,3,2,1,0]
# Be sure to catch the exception that will be generated for 1/0

list = [5, 4, 3, 2, 1, 0]

for n in list:
    try:
        print(1 / n)
    except ZeroDivisionError:
        print("You can't divide by zero!")
