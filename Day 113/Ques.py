# Ques : Given an input string, determine if it contains any alphanumeric characters, alphabetical characters, digits, lowercase letters, or uppercase letters respectively.

if __name__ == '__main__': 
    s = input() 
    print(any(c.isalnum() for c in s)) 
    print(any(c.isalpha() for c in s)) 
    print(any(c.isdigit() for c in s)) 
    print(any(c.islower() for c in s)) 
    print(any(c.isupper() for c in s))