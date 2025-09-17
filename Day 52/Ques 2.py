# Question: This is an information page explaining the numpy.identity and numpy.eye functions.
# numpy.identity(n): Returns an identity array (square matrix with 1s on the main diagonal and 0s elsewhere).
# numpy.eye(N, M, k): Returns a 2-D array with 1s on the diagonal and 0s elsewhere. k determines the diagonal.

import numpy
numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(numpy.eye(n, m, k=0))
