# input & output example
name = input("What is your name? ")
print(name)
print("Hello", name, "!", sep="+", end="")

# Important Keys

# New line
print("\n")
# Tab
print("\t")

# f strings
print(f"Hello, {name}!")

# string formatting & type casting
age = int(input("How old are you? "))
print(f"You will be {age + 1} years old next year.")

# types
am_i_hungry = True
am_i_hungry_type = type(am_i_hungry)

print(am_i_hungry_type)
print(f"{am_i_hungry_type = }")
