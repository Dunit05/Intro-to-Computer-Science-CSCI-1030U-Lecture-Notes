print("Question 1:")


def reverse_rec(str):
    if len(str) < 1:
        return str

    return reverse_rec(str[1:]) + str[0]


print('reverse_rec("CSCI 1030U"):', reverse_rec("CSCI 1030U"))
# 'U0301 ICSC'
print('reverse_rec("Python!"):', reverse_rec("Python!"))
# '!nohtyP'

print("Question 2:")


def palindrome_rec(str):
    if len(str) < 2:
        return True

    if str[0] != str[len(str) - 1]:
        return False

    return palindrome_rec(str[1 : len(str) - 1])


print("is level a palindrone?", palindrome_rec("level"))
# True
print("is lever a palindrone?", palindrome_rec("lever"))
# False


# Question 3
class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def getShippingCost(self):
        return self.weight * 10

    def getTax(self):
        return self.price * 0.13

    def getTotalPrice(self):
        return self.price + self.getShippingCost() + self.getTax()


razor = Product("Electric Razor", 49.99, 0.25)
homeGym = Product("Home Gym", 879.99, 115.0)
print("total cost of", razor.name, ":", razor.getTotalPrice())
# 58.9887
print("total cost of", homeGym.name, ":", homeGym.getTotalPrice())
# 2144.3887

print("Question 4:")


class StudentEntry:
    def __init__(self, name, sid):
        self.labs = 0.0
        self.assignments = 0.0
        self.midterm = 0.0
        self.final = 0.0
        self.name = name
        self.sid = sid

    def average(self):
        return (
            self.labs
            + self.assignments
            + (30.0 * self.midterm) / 100.0
            + (40.0 * self.final) / 100.0
        )

    def letterGrade(self):
        mark = self.average()
        print("Mark: ", mark)
        if mark < 50:
            return "F"
        elif mark < 60:
            return "D"
        elif mark < 70:
            return "C"
        elif mark < 80:
            return "B"
        else:
            return "A"


bsmith = StudentEntry("Bob Smith", "1000001")
bsmith.labs = 9.0
bsmith.assignments = 17.0
bsmith.midterm = 57.5
bsmith.final = 60.0
print("Bob Smith: ", bsmith.letterGrade())
# C

sjones = StudentEntry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5
print("Sally Jones: ", sjones.letterGrade())
# A

print("Question 5:")


class KeyNotFoundError(Exception):
    pass


class Dictionary:
    def __init__(self):
        self.keys_and_values = []

    def get(self, key_to_find):
        for key, value in self.keys_and_values:
            if key == key_to_find:
                return value

        raise KeyNotFoundError(f"Key not found: {key_to_find}")

    def set(self, key, value):
        self.keys_and_values.append((key, value))

    def __str__(self):
        result = "["
        for key, value in self.keys_and_values:
            if len(result) == 1:
                result += f"({key}, {value})"
            else:
                result += f", ({key}, {value})"
        result += "]"
        return result


products = Dictionary()
products.set("RTX3060", 329.99)
products.set("RTX3070", 499.99)
products.set("RTX3080", 1499.99)
products.set("RTX3090", 1999.99)
print(f"products = {products}")
# output: products = [('RTX3060', 329.99), ('RTX3070', 499.99),
# ('RTX3080', 1499.99), ('RTX3090', 1999.99)]
print(f'RTX3090 = {products.get("RTX3090")}')
# output: RTX3090 = 1999.99
try:
    print(f'RTX3050 = {products.get("RTX3050")}')
except KeyNotFoundError as error:
    print(f"Cannot find key: {error}")
# output: Cannot find key: Key not found: RTX3050


print("Question 6:")

import math


def math1(x, n, max_n):
    total = 0.0

    for i in range(n, max_n + 1):
        term = math.pow(-1, i) * math.pow(x, i) / math.factorial(i)
        total += term

    return total


print(f"{math1(0.0, n = 0, max_n = 10) = }")
# output: math1(0.0, n = 0, max_n = 10) = 1.0

print(f"{math1(0.5, n = 0, max_n = 10) = }")
# output: math1(0.5, n = 0, max_n = 10) = 0.606530659724375

print("Question 7:")


def math2(x, n, max_n):
    total = 0.0

    for i in range(n, max_n + 1):
        term = (
            2
            * math.pow(-1, i)
            * math.pow(x, 2 * i + 1)
            / (math.sqrt(math.pi) * (2 * i + 1) * math.factorial(i))
        )
        total += term

    return total


print(f"{math2(0.0, n = 0, max_n = 10) = }")
# output: math2(0.0, n = 0, max_n = 10) = 0.0

print(f"{math2(0.5, n = 0, max_n = 10) = }")
# output: math2(0.5, n = 0, max_n = 10) = 0.5204998778130467
