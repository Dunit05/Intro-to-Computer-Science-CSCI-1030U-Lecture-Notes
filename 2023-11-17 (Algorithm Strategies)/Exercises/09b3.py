# Write the dynamic programming solution to the Fibonacci numbers problem in Python


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
