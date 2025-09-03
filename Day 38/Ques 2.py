# Question: You are given two arrays, A and B, with dimensions N x N. Your task is to compute their matrix product.

import numpy

n = int(input())
A = numpy.array([list(map(int, input().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(n)])
result = numpy.matmul(A, B)
print(result)