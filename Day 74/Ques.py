# Compress the String :In this task, you're asked to appreciate the usefulness of the groupby() function of itertools.
# You are given a string S. Suppose a character c occurs consecutively X times in the string. Replace these consecutive occurrences of the character c with (X,c) in the string.

from itertools import groupby
s = input().strip()
print(' '.join(f"({len(list(g))}, {k})" for k, g in groupby(s)))