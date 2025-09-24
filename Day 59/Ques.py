# Question: Given a string s, use Python's built-in string validation methods to check if it contains any alphanumeric characters, any alphabetical characters, any digits, any lowercase characters, and any uppercase characters.

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))