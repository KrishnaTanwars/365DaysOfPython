# Ques : You are given N email addresses; keep only those that match the valid format username@website.extension.
# Validate using rules for allowed characters, extension length ≤ 3, and print them in lexicographical order.4

import re

def fun(s):
    # username: letters, digits, -, _
    # website: letters, digits
    # extension: letters, length <= 3
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, s) is not None

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = [input().strip() for _ in range(n)]
    
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
