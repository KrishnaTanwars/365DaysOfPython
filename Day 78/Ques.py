# Question : Given N email addresses, print a list of only valid email addresses in lexicographical order. An email is valid if:

import re

def fun(s):
    # Regex checks for:
    # 1. Username: [a-zA-Z0-9_-]+
    # 2. @
    # 3. Website Name: [a-zA-Z0-9]+
    # 4. .
    # 5. Extension: [a-zA-Z]{1,3} (maximum length 3)
    return bool(re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s))

def filter_mail(emails):
    # Use the filter function with the validation function 'fun'
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    
    # Get filtered list, sort it lexicographically, and print
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)