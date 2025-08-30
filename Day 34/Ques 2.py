# Question: You are given N email addresses. Your task is to filter out the valid ones and print them in a sorted list. A valid email has the format username@websitename.extension where the username consists of letters, digits, dashes, and underscores; the website name consists of letters and digits; and the extension has a maximum length of 3.


import re

def fun(s):
    # Checks if the email address is valid based on the defined pattern.
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, s) is not None

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)