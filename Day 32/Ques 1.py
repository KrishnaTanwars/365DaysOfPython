# Question: You are given a string N. Your task is to verify that N is a valid floating point number. A valid number must start with +, -, or . symbol, contain at least one decimal value, and have exactly one . symbol.

import re

t = int(input())
pattern = r'^[+-]?(\d+\.\d+|\.\d+)$'

for _ in range(t):
    s = input().strip()
    if re.match(pattern, s):
        try:
            float(s)
            print(True)
        except:
            print(False)
    else:
        print(False)