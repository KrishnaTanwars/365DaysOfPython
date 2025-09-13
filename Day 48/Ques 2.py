# Question: Given a name and an email address, print the name and email address if the email address is valid.

import re
import email.utils

n = int(input())
pattern = re.compile(r"^[a-zA-Z][\w\-\._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
for _ in range(n):
    s = input().strip()
    name, addr = email.utils.parseaddr(s)
    if pattern.match(addr):
        print(email.utils.formataddr((name, addr)))
