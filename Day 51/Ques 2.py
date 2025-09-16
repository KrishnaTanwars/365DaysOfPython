# Question: Given the shape of an array in the form of space-separated integers, print an array of the given shape and integer type using the numpy.zeros and numpy.ones tools.

import numpy as np

shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
