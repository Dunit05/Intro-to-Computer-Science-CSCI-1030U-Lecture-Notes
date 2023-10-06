# Write a recursive implementation to calculate the Fibonacci numbers
# Recall the definition of the Fibonacci numbers is:

# Fib n = 	n, if n == 0 or n == 1
# 		   Fib(n-1) + Fib(n-2), if n > 1

# 0, 1, 1, 2, 3, 5, 8, 13, 21, …


def fib(n):
    # Base Case
    if n == 0 or n == 1:
        return n
    # Recursive Case
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
