# Write some code to ask the user their age, and raise a custom exception if they are not yet 18 years old


class AgeError(Exception):
    pass


age = int(input("How old are you? "))
if age < 18:
    raise AgeError("You must be 18 years old to use this program.")
