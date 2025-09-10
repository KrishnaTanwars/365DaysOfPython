# Question: You are given a string S and a string k. Find the indices of the start and end of the substring k in S. If no match is found, print (-1, -1).

import re

s = input()
k = input()
pattern = re.compile(r'(?='+ re.escape(k) + ')')
matches = list(pattern.finditer(s))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))