# Ques: Given a string and a substring, print the number of times the substring occurs in the given string. The traversal should be from left to right.

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count