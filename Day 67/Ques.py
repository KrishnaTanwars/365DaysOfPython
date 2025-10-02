# Question : You need to write a program to validate credit card numbers based on the following rules:

# It must start with a 4, 5, or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4, separated by one hyphen '-'.
# It must NOT use any other separator like ' ', '_', etc.
# It must NOT have 4 or more consecutive repeated digits.

import re

n = int(input())
for _ in range(n):
    card = input().strip()
    if re.match(r"^[456]\d{15}$|^[456]\d{3}(?:\-\d{4}){3}$", card) and not re.search(r"(\d)\1{3}", card.replace('-', '')):
        print("Valid")
    else:
        print("Invalid")
