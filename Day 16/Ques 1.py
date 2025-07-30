# 🧾 Question: Given a string S and an integer k, print all combinations from length 1 to k in lexicographic order.

# 💻 Code:

from itertools import combinations

S, k = input().split()
k = int(k)
S = sorted(S)

for i in range(1, k + 1):
    for comb in combinations(S, i):
        print(''.join(comb))