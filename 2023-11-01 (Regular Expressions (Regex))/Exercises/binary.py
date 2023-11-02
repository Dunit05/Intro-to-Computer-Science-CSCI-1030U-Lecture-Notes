# Write a Python program to recognize a binary number of 8 or 16 bits

import re


def binary(string):
    pattern = re.compile("^[01]{8}$|^[01]{16}$")
    if re.search(pattern, string):
        return True
    else:
        return False


print(binary("01010101"))
print(binary("010101010101010"))
