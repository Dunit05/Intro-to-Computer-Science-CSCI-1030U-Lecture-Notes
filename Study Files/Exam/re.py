# Write a regular expression to recognize any string belonging to the following language:

# Between 3 and 5 As (inclusive), followed by an optional B, then zero or more Cs, then either a single D or one or more Es

# Below are some examples of strings that would be a part of this language:

# AAABCCCD
# AAAAEEEE
# AAAAABD
# AAACCCE
# Note: Do not include any spaces or unnecessary parentheses in your answer.

# Note: You are not required to write any Python code, only the regular expression itself (without quotes).
# ^A{3,5}B?C*D?E+$

# -----

# Write a regular expression to recognize a basic street address, briefly described as follows

# One or more digits (0-9) followed by one or more words, each of which is one or more upper or lowercase letters, separated by spaces.

# Below are some examples of strings that would be a part of this language:

# 2000 Simcoe Road North
# 290 Bremner Blvd
# 123 Apple
# Note: Do not include any spaces or unnecessary parentheses in your answer.

# Note: You are not required to write any Python code, only the regular expression itself (without quotes).
# ^\d+([A-Za-z]+\s?)+

# -----

# Write a regular expression based on this finite automaton:

# Below are some examples of strings that would be a part of this language:

# 11{...}100{...}01
# 00{...}00

# Note: You are not required to write any Python code, only the regular expression itself (without quotes).
# ^11(1|0)*100(1|0)*01$|^00(1|0)*00$

# -----

# Which algorithm strategy does the following algorithm use?

# def get_longest_prefix(str1, str2):
#     if len(str1) > len(str2):
#         prefix = str1[:len(str2)]
#     else:
#         prefix = str1

#     while len(prefix) > 0:
#         if str2.startswith(prefix):
#             return prefix
#         prefix = prefix[:len(prefix) - 1]

#     return ''

# dynamic programming

# greedy

# none of the above

# divide and conquer
# greedy

# -----

# The following is a binary tree: 11, 7, 23, 4, 8, 19, 31
# Which value would be the parent of the node containing the value 19?
# 23

# -----

# The following is a binary tree: 11, 7, 23, 4, 8, 19, 31
# Which value would be the right child of the 7
# 8

# -----
# The following is a binary tree: 11, 7, 23, 4, 8, 19, 31
# Which value would be the left child of the 11
# 7
