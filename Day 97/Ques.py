# Ques : Given a string s and integer k, split s into equal parts of length k and remove duplicate characters from each part while keeping their order. Print each resulting substring on a new line.

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique = ""
        for ch in substring:
            if ch not in unique:
                unique += ch
        print(unique)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)