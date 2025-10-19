# Ques : Count how many times a substring occurs in a string (case-sensitive).

c = 0
def count_substring(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            c += 1
    return c
