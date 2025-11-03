# Ques : Given a string s, convert all lowercase letters to uppercase and all uppercase letters to lowercase. Return the modified string after swapping the cases.

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)