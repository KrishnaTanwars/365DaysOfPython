# Ques : Compute the probability that at least one of the chosen k indices contains the letter 'a'.

from itertools import combinations

n = int(input())
arr = input().split()
k = int(input())

total = 0
good = 0

for comb in combinations(range(n), k):
    total += 1
    if any(arr[i] == 'a' for i in comb):
        good += 1

print(f"{good/total:.4f}")
