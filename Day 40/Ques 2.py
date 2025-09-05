# Question: Given a 2D array, find the minimum value along axis 1 (rows) and then find the maximum value of those minimums.

import numpy as np

n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.max(np.min(arr, axis=1)))