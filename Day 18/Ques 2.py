# Problem: Given two integers a and b, print: a//b, a%b divmod(a, b)

# Input:
# First line: a
# Second line: b

a = int(input())
b = int(input())

print(a // b)        # quotient
print(a % b)         # remainder
print(divmod(a, b))  # tuple (quotient, remainder)