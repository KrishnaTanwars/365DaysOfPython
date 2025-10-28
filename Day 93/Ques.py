# Ques : Given a string s and an integer k (where length of s is a multiple of k), split s into equal parts of size k.
# For each part, remove duplicate characters while keeping their first occurrence order, and print the result for each part on a new line.

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique = ""
        for ch in substring:
            if ch not in unique:
                unique += ch
        print(unique)

if __name__ == '__main__':
    s = input()
    k = int(input())
    merge_the_tools(s, k)
