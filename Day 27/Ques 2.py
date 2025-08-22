# Question: For a given integer N, print a palindromic triangle of size N. You must use only one print statement inside the given for loop.

for i in range(1, int(input()) + 1):
    print((10**i // 9)**2)