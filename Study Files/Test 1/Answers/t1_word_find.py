# Tommy D. Michailidis
# #100911141, Midterm 1


# Function find_longest_string_with_a(strings)
def find_longest_string_with_a(strings):
    # Create & Initialize a new temp List
    newlist = []
    # Iterate though each string in strings
    for string in strings:
        # If there is a latter "a" in string
        if "a" in string:
            # add the string to the temp list
            newlist.append(string)
    # return the longest string containing "a" using key=len
    return max(newlist, key=len)


# ! Testing
print(
    find_longest_string_with_a(
        [
            "always",
            "the",
            "longest",
            "string",
            "is",
            "best",
            "applied",
            "to",
            "hunting",
            "ducks",
            "everywhere",
        ]
    )
)

print(
    find_longest_string_with_a(
        ["act", "now", "to", "invite", "a", "duck", "to", "be", "your", "best", "bud"]
    )
)
