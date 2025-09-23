# Question: The problem asks to check a string for various character types using Python's built-in string validation methods. The code provided checks if the string contains at least one alphanumeric, alphabetic, digit, lowercase, and uppercase character.

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))