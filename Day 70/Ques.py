# Question (Python/Regex): Write a Python solution to validate a credit card number from an imaginary company ABCD Bank based on the following characteristics:

# It must start with 4, 5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have groups of 4, separated by one hyphen -.
# It must NOT use any other separator (like space, comma, etc.).
# It must NOT have 4 or more consecutive repeated digits.

import re

for _ in range(int(input())):
    s = input().strip()
    # Check for rules 1-5 (start with 4-6, 16 digits, digits/hyphen only, valid grouping)
    if not re.match(r"^[4-6]\d{3}([\-]?)\d{4}([\-]?)\d{4}([\-]?)\d{4}$", s):
        print("Invalid")
    # Check for rule 6 (4 or more consecutive repeated digits)
    elif re.search(r"(\d)(\-?\1){3,}", s.replace("-", "")):
        print("Invalid")
    else:
        print("Valid")