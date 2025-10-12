# Question : Given N email addresses, print only the valid ones in lexicographical order using Python's filter() function.

import re

def fun(s):
    # Regex to match the rules:
    # 1. Username: [a-zA-Z0-9_]+
    # 2. @
    # 3. Website Name: [a-zA-Z0-9]+
    # 4. .
    # 5. Extension (max length 3): [a-zA-Z]{1,3}
    return bool(re.match(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))

def filter_mail(emails):
    # Use filter() with a lambda or the defined fun
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
