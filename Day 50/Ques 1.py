# Question: Validate a given postal code P based on two rules:
# P must be a number between 100000 and 999999.
# P cannot contain more than one alternating repetitive digit pair.
# The user needs to provide the regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair.

import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

P = input()

print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)