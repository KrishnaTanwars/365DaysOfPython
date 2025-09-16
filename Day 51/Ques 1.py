# Question: Given an N×M integer array matrix with space-separated elements, print the transpose and flatten results.

import numpy as np

n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.transpose(arr))
print(arr.flatten())
