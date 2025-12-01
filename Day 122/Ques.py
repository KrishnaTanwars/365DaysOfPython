# Ques : Given a numeric string S, compress each group of consecutive identical digits.
# Print each group as (count, digit) separated by spaces.

from itertools import groupby

s = input().strip()
print(*( (len(list(g)), int(k)) for k, g in groupby(s) ))
