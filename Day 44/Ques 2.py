# Question: Given a string S containing alphanumeric characters, spaces, and symbols, find all substrings that contain 2 or more vowels. These substrings must lie between 2 consonants and should contain vowels only.

import re

s = input().strip()
pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
matches = re.findall(pattern, s)

if matches:
    for n in matches:
        print(n)
else:
    print(-1)
