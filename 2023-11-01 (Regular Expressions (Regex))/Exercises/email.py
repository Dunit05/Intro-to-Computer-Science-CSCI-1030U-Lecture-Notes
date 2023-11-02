# Write a Python program to recognize a simple E-Mail address
# e.g. bsmith@gmail.com
# e.g. randy.fortier@ontariotechu.net
# e.g. candy_canes1@sweets.co.uk

import re


def email(email):
    pattern = re.compile("^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\\.[a-zA-Z]{2,3}$")
    if re.search(pattern, email):
        return True
    else:
        return False


print(email("bsmith@gmail.com"))
print(email("bsmith"))
print(email("randy.fortier@ontariotechu.net"))
print(email("candy_canes1@sweets.co.uk"))
