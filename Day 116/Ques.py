# Ques : Validate credit card numbers using regex based on given rules (start with 4/5/6, 16 digits, optional hyphens in groups of 4, digits only, and no 4+ repeated digits).

import re

n = int(input())
for _ in range(n):
    s = input().strip()
    if not re.match(r'^(?:[456]\d{15}|[456]\d{3}(?:-\d{4}){3})$', s):
        print("Invalid")
        continue
    t = s.replace("-", "")
    print("Invalid" if re.search(r'(\d)\1{3,}', t) else "Valid")
