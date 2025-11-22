# Ques : Validate credit card numbers that start with 4, 5, or 6, contain exactly 16 digits (optionally in XXXX-XXXX-XXXX-XXXX format), and use only digits or single hyphens.
# They must not include other separators or any digit repeating 4 or more times consecutively.

import re

n=int(input())
for _ in range(n):
    s=input().strip()
    if not re.match(r'^(?:[456]\d{15}|[456]\d{3}(?:-\d{4}){3})$',s):
        print("Invalid");continue
    t=s.replace("-","")
    print("Invalid" if re.search(r'(\d)\1{3,}',t) else "Valid")
