# Question: Find the first occurrence of a repeating alphanumeric character in a given string. If a repeating character is found, print that character; otherwise, print -1.

import re

s = input()
match = re.search(r'([a-zA-Z0-9])\1', s)

if match:
    print(match.group(1))
else:
    print(-1)











Tools

