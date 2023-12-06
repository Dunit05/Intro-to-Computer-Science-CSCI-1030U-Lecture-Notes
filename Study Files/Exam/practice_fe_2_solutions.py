# Question 1
def sum_of_squares(min, max):
    sum = 0
    
    for val in range(min, max+1):
        sum += val ** 2

    return sum

print(f'sum_of_squares(1,10): {sum_of_squares(1,10)}')
# output: sum_of_squares(1,10): 385

print(f'sum_of_squares(1,5): {sum_of_squares(1,5)}')
# output: sum_of_squares(1,5): 55

# Question 2
def get_factors(n):
    factors = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

print(f'Factors of 12: {get_factors(12)}')
# output: Factors of 12: [1, 2, 3, 4, 6, 12]

print(f'Factors of 20: {get_factors(20)}')
# output: Factors of 20: [1, 2, 4, 5, 10, 20]

print(f'Factors of 100: {get_factors(100)}')
# output: [1, 2, 4, 5, 10, 20, 25, 50, 100]

# Question 3
def get_powers_of_2(n):
    if n == 0:
        return [1]
    
    return get_powers_of_2(n - 1) + [2 ** n]

print(f'2^0 .. 2^4: {get_powers_of_2(4)}')
# output: [1, 2, 4, 8, 16]

print(f'2^0 .. 2^10: {get_powers_of_2(10)}')
# output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# Question 4
def are_equal(list1, list2):
    # there are many easier ways to do this, but I'll consider this the canonical way to do it
    for element in list1:
        if element not in list2:
            return False

    for element in list2:
        if element not in list1:
            return False

    return True

print(f'are_equal([1,2,3], [3,1,2]): {are_equal([1,2,3], [3,1,2])}')
# are_equal([1,2,3], [3,1,2]): True

print(f'are_equal([1,2,3], [4,1,3]): {are_equal([1,2,3], [4,1,3])}')
# are_equal([1,2,3], [4,1,3]): False

print(f'are_equal([1,8,15], [1,15,8]): {are_equal([1,8,15], [1,15,8])}')
# are_equal([1,8,15], [1,15,8]): True

# Question 5
def is_prime(val):
    if val == 0:
        return False
    
    for div in range(2, val//2):
        if val % div == 0:
            return False
    return True

def filter_primes(elements):
    if len(elements) == 0:
        return []
    
    if is_prime(elements[0]):
        return [elements[0]] + filter_primes(elements[1:])
    else:
        return filter_primes(elements[1:])

print(f'filter_primes(range(20)): {filter_primes(range(20))}')
# output:  filter_primes(range(20)): [2, 3, 4, 5, 7, 11, 13, 17, 19]

print(f'filter_primes(range(100,200)): {filter_primes(range(100,200))}')
# output:  filter_primes(range(100,200)): [101, 103, 107, 109, 113, 127,
#          131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
#          193, 197, 199]

# Question 6
import math

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_distance_to(self, other_point):
        return math.sqrt(math.pow(self.x - other_point.x, 2) + 
                         math.pow(self.y - other_point.y, 2) +
                         math.pow(self.z - other_point.z, 2))

p1 = Point3D(2.0, 2.0, 4.0)
p2 = Point3D(3.0, 1.0, 2.0)

print(f'distance between p1 and p2: {p1.get_distance_to(p2)}')
# output:  distance between p1 and p2: 2.44948974278

# Question 7
def dc_find(values, to_find):
    if len(values) == 0:
        return False
    elif len(values) == 1:
        return to_find == values[0]
    
    middle = len(values) // 2
    found_left = dc_find(values[:middle], to_find)
    found_right = dc_find(values[middle:], to_find)
    return found_left or found_right

print(f'dc_find([1,13,5,7,9,15], 8) == {dc_find([1,13,5,7,9,15], 8)}')
# output: dc_find([1,13,5,7,9,15], 8) == False

print(f'dc_find([1,13,5,7,9,15], 13) == {dc_find([1,13,5,7,9,15], 13)}')
# output: dc_find([1,13,5,7,9,15], 13) == True

# Question 8
def greedy_change(amount, denoms):
    change = []
    
    for denom in denoms[::-1]:
        while amount >= denom:
            change.append(denom)
            amount -= denom
    
    return change

denoms = [1,2,5,10,20,50]

print(f'greedy_change(174, {denoms}) == {greedy_change(174, denoms)}')
# output: greedy_change(174, [1,2,5,10,20,50]) == [50, 50, 50, 20, 2, 2]

print(f'greedy_change(99, {denoms}) == {greedy_change(99, denoms)}')
# output: greedy_change(99, [1,2,5,10,20,50]) == [50, 20, 20, 5, 2, 2]

# Question 9
'''
def towers_of_hanoi(n, start, end, temp):
    if n < 1:
        return

    towers_of_hanoi(n - 1, start, temp, end)

    print('Move 1 ring from', start, 'to', end) # count this line only

    towers_of_hanoi(n - 1, temp, end, start)
'''
def towers_of_hanoi(n, start, end, temp):
    if n < 1:
        return 0

    op_count = towers_of_hanoi(n - 1, start, temp, end)

    print('Move 1 ring from', start, 'to', end) # count this line only
    op_count += 1

    op_count += towers_of_hanoi(n - 1, temp, end, start)

    return op_count

'''
best guess:  2^n
n   prints
----------
1   1
2   3
3   7
4   15
5   31
6   63
7   127
8   255
'''
results = []
for n in range(1, 9):
    op_count = towers_of_hanoi(n, 0, 1, 2)
    results.append((n, op_count))
print(results)

# Question 10
import json

def create_summary(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        min_price = 100000.0
        min_product = ''
        max_price = 0.0
        max_product = ''
        price_sum = 0.0
        price_count = 0

        for line in input_file:
            data = line.split(',')
            price = float(data[3])

            if price < min_price:
                min_price = price
                min_product = data[1]

            if price > max_price:
                max_price = price
                max_product = data[1]

            price_sum += price
            price_count += 1

        summary = {
            "cheapest_product": min_product,
            "costliest_product": max_product,
            "average_price": price_sum / price_count
        }

        with open(output_filename, 'w') as output_file:
           json.dump(summary, output_file)

create_summary('input_data.txt', 'results.json')

# Question 11
class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_shipping_cost(self):
        return self.weight * 10

    def get_tax(self):
        return self.price * 0.13

    def get_total_price(self):
        return self.price + self.get_shipping_cost() + self.get_tax()

import unittest

class Product_Test(unittest.TestCase):
    def test_get_shipping_cost(self):
        product1 = Product('RTX3090', 1999.99, 0.5)
        self.assertEqual(product1.get_shipping_cost(), 5.0)

        product2 = Product('RTX3060', 699.99, 0.35)
        self.assertEqual(product2.get_shipping_cost(), 3.5)

    def test_get_tax(self):
        product1 = Product('RTX3090', 1999.99, 0.5)
        self.assertAlmostEqual(product1.get_tax(), 260.00, places=2)

        product2 = Product('RTX3060', 699.99, 0.35)
        self.assertAlmostEqual(product2.get_tax(), 91.00, places=2)

    def test_get_total_price(self):
        product1 = Product('RTX3090', 1999.99, 0.5)
        self.assertAlmostEqual(product1.get_total_price(), 2264.99, places=2)

        product2 = Product('RTX3060', 699.99, 0.35)
        self.assertAlmostEqual(product2.get_total_price(), 794.49, places=2)

if __name__ == '__main__':
    unittest.main()