# Ques: Given integers a, b, and m, print a^b and (a^b) % m using Python's pow() function.

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))

