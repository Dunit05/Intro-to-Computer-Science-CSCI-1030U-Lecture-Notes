# For this question, create a file called practice_searching.py.  In this file, define two functions:

# has_no_repeated_letter - takes a single string (string), and uses recursion to determine if it contains any character more than once
# Returns True, if string has no repeating characters (e.g. abcdefghi would return True)
# Returns False, if string has one or more repeating characters (e.g. aaa would return False, abcdaf would also return False)
# Do not use regular expressions for this question
# If you do not use recursion, you will only get part marks
# get_longest_matching_substring - takes a string (string) and a single-argument function (check_match), and finds the longest substring within string that, when passed to check_match(), would produce a True return value
# If there are no matches, raise a custom exception (NoMatchFoundException)
# Hint:  You can use brute force to check every possible substring of string for this function


class NoMatchFoundException(Exception):
    pass


def has_no_repeated_letter(string):
    if string == "":
        return True
    else:
        if string[0] in string[1:]:
            return False
        else:
            return has_no_repeated_letter(string[1:])


def get_longest_matching_substring(string, check_match):
    if string == "":
        raise NoMatchFoundException()
    else:
        for i in range(len(string)):
            if check_match(string[:i]):
                return string[:i]
        return get_longest_matching_substring(string[1:], check_match)


print("ablewasiereisawelba:", has_no_repeated_letter("ablewasiereisawelba"))
# expected output: ablewasiereisawelba: False

print("abcd:", has_no_repeated_letter("abcd"))
# expected output: abcd: True

print(
    "longest with no repeated letter:",
    get_longest_matching_substring(
        "i saw abba, but ablewasiereisawelba by the racecar", has_no_repeated_letter
    ),
)
# expected output: longest with no repeated letter: ut ablew
