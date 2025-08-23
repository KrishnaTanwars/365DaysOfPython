# Question: You are given a list of N lowercase English letters. For a given integer K, you select K indices from a uniform random distribution. Find the probability that at least one of the K indices selected contains the letter 'a'.

import math

n = int(input().strip())
letters = input().split()
k = int(input().strip())

count_a = letters.count('a')
total = math.comb(n, k)
no_a = math.comb(n - count_a, k) if n - count_a >= k else 0
prob = 1 - no_a / total
print(f"{prob:.4f}")
