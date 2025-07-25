# Q2: Cartesian Product of Two Lists
# Description:
# You are given two lists A and B. Compute and print their Cartesian Product.
# Example: A = [1, 2], B = [3, 4] → Output: (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

# Input
A = list(map(int, input("Enter list A elements: ").split()))
B = list(map(int, input("Enter list B elements: ").split()))

# Cartesian Product
result = list(product(A, B))

# Output
print(*result)
