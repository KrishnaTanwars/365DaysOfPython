# Question: Given N lines of CSS code, find and print all valid Hex Color Codes that are inside CSS declaration blocks. A valid code starts with '#', has 3 or 6 hex characters (0-9, a-f, A-F), and is not part of the selector.

import re

n = int(input())
inside_block = False
for _ in range(n):
    line = input()
    if '{' in line:
        inside_block = True
    elif '}' in line:
        inside_block = False
    elif inside_block:
        # findall will look for all occurrences of the pattern in the line
        matches = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})', line)
        for code in matches:
            print(f"#{code}")
