# Problem: Given a 2-D array of dimensions N x M, perform the sum over axis 0 and then find the prod of the resulting 1-D array.

import numpy

n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.prod(numpy.sum(arr, axis=0)))