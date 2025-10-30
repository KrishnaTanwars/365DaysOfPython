# Ques:Change a character at a given index in a string and print the modified string.

s = input(); i, c = input().split()
print(s[:int(i)] + c + s[int(i)+1:])
