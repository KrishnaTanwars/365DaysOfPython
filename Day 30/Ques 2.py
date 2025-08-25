# Question: You are given a polynomial P of a single indeterminate (or variable), x. You are also given the values of x and k. Your task is to verify if P(x)=k.

x, k = map(int, input().split())
P = input()

if eval(P) == k:
    print(True)
else:
    print(False)