# Question: Given an integer N, print a numerical triangle of height N−1 using only arithmetic operations, a single for loop, and one print statement. (e.g., for N=5, output is 1, 22, 333, 4444).

for i in range(1, int(input())):
    print((10**i // 9) * i)