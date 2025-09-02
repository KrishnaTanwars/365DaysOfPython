# Question: You are given a space-separated list of numbers. Your task is to print a reversed NumPy array with the element type float.

import numpy

def arrays(arr):
    # Convert list to a numpy array of type float and reverse it
    return numpy.array(arr, float)[::-1]

# Read space-separated input and split into a list
arr = input().strip().split(' ')
result = arrays(arr)
print(result)