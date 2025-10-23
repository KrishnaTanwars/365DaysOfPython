# Ques : Given a string s, check if it contains any alphanumeric, alphabetical, digit, lowercase, and uppercase characters. Print True or False for each check.

s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
