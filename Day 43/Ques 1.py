# Question: Perform basic mathematical operations (addition, subtraction, multiplication, integer division, modulo, and power) on two NumPy arrays.

import numpy as np
n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)