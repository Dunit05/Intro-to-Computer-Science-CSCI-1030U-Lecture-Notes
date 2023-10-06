# Create a recursive version of the factorial function

# Don’t forget an exit condition!

# n! = 	1, if n == 0 or n == 1
# 		n * (n - 1)!, if n > 1


def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)


print(factorial(5))
