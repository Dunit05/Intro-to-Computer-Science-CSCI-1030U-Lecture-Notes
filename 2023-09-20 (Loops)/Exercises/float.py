# Write the code which, given a positive floating point number x, returns a value that is close to the value of exp(x) using the following formula, without using the factorial function:
# e = 1 + x + x^2/2! + x^3/3! + ... + x^n/n!
import math

x = float(input("Enter a positive floating point number: "))
e = 1

for n in range(0, 10):
    e += x**n / math.factorial(n)
print(f"e^{x} is approximately {e}")

# Write the code which, given a positive floating point number x, returns a value that is close to the value of sin x
# Use the following convergent series: sin x = x - x^3/3! + x^5/5! - x^7/7! + ...

x = float(input("Enter a positive floating point number: "))
sin = x

for n in range(1, 50):
    sin += (-1) ** n * x ** (2 * n + 1) / math.factorial(2 * n + 1)

print(f"sin({x}) is approximately {sin}")

# Write the code which, given a positive floating point number x, returns a value that is close to the square root of x
# Method:
# Guess any square root estimate
# Determine if the square of that estimate is too high or too low
# Add or subtract from that estimate to bring it closer to the right answer

x = float(input("Enter a positive floating point number: "))
guess = x / 2

for n in range(1, 10):
    guess = (guess + x / guess) / 2

print(f"The square root of {x} is approximately {guess}")
