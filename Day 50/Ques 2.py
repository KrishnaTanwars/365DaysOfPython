# Question: The user wants to understand how to use np.array.shape to get the dimensions of a NumPy array and np.array.reshape() to change its dimensions.

import numpy as np

arr = np.array(list(map(int, input().split())))
print(arr.reshape(3, 3))
