'''🐍 Q2. Print Full Name

🔹 Problem:
Given first name and last name as input, print:

Hello <firstname> <lastname>! You just delved into python.'''


# ✅ Code:

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print_full_name(first_name, last_name)
