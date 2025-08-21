# Question: You are given a string S consisting of digits. Your task is to compress the string by replacing consecutive occurrences of a character with (X,c), where X is the number of occurrences and c is the character.

from itertools import groupby

s = input().strip()
print(*[(len(list(g)), int(k)) for k, g in groupby(s)])