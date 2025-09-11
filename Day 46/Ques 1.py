# Question: Check if a given 10-digit number is a valid mobile number, which starts with a 7, 8, or 9.

import re
n = int(input())
for _ in range(n):
    s = input().strip()
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")