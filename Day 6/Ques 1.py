'''🐍 Q1. Swap Case
🔹 Problem:
Take a string input and swap the case of each character — uppercase becomes lowercase and vice versa.'''

#✅ Code:

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input("Enter a string: ")
    result = swap_case(s)
    print(result)
