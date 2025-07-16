# Problem Statement (Summary):
# A shoe shop owner has X number of shoes with different sizes.
# There are N customers; each customer offers a price for a specific shoe size.
# If the size is available, he sells and earns the price.
# Calculate the total money earned.

# Input Format:

# First line: Integer X

# Second line: List of shoe sizes

# Third line: Integer N

# Next N lines: Two integers - desired size and offered price

from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_inventory = Counter(shoe_sizes)

N = int(input())
earning = 0

for _ in range(N):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        earning += price
        shoe_inventory[size] -= 1

print(earning)
