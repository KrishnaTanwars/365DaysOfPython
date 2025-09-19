# Question: Count the number of times a given substring occurs in a string. The traversal should be from left to right, and the search is case-sensitive.

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count