# Ques : Compress the string by replacing each group of consecutive identical digits with a tuple (count, digit) using itertools.groupby().

from itertools import groupby

s = input().strip()
print(*( (len(list(g)), int(k)) for k, g in groupby(s) ))
