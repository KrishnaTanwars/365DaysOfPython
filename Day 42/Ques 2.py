# Problem: Given a 1-D array A, print the floor, ceil, and rint of all elements.

import numpy

numpy.set_printoptions(sign=' ')

arr = numpy.array(list(map(float, input().split())))

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))