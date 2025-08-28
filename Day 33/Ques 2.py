# Question: You are given a string N. Your task is to verify that N is a valid floating-point number. A valid number can start with +, -, or .; must contain at least one decimal value; and must have exactly one . symbol.

import re

t = int(input())
pattern = r'^[+-]?(\d*\.\d+)$'

for _ in range(t):
    s = input().strip()
    try:
        if re.match(pattern, s):
            float(s)
            print(True)
        else:
            print(False)
    except:
        print(False)

