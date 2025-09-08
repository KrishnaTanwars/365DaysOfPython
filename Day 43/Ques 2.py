# Question: Concatenate two or more NumPy arrays. The user's provided code also demonstrates how to concatenate arrays along a specified axis.

import numpy as np
n, m, p = map(int, input().split())
array_1 = np.array([list(map(int, input().split())) for _ in range(n)])
array_2 = np.array([list(map(int, input().split())) for _ in range(m)])
result = np.concatenate((array_1, array_2), axis=0)
print(result)