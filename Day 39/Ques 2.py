# Ques : You are given a square matrix A with dimensions NtimesN. Your task is to find its determinant. Round the answer to 2 decimal places.

import numpy as np

n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]

det = np.linalg.det(matrix)
print(round(det, 2))