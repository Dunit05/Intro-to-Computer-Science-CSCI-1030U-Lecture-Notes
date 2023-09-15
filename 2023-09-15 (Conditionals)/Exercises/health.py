# Write a program that checks the value of the health_points variable
# If health_points is less than or equal to 0, then set the variable is_dead to True
# If health_points is greater than 0, then set the variable is_dead to False

health_points = 0
is_dead = False

if health_points <= 0:
    is_dead = True
else:
    is_dead = False

# True if health_points <= 0 else False <-- Ternary operator

print("You are dead" if True else "You are alive")  # <-- Ternary operator

# if True: <-- Same as ternary operator
#     print("You are dead")
# else:
#     print("You are alive")
