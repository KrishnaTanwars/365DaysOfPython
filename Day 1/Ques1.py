# 🚀 Problem: 3D Coordinates List using List Comprehension
# Given integers x, y, z, and n, print a list of all [i, j, k] such that:

# 0 ≤ i ≤ x

# 0 ≤ j ≤ y

# 0 ≤ k ≤ z

# But i + j + k != n

# Use list comprehension. Print in lexicographic order.

x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = [
    [i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if (i + j + k != n)
]
print(result)
