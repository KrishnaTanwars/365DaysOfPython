# Question: For a given number of test cases, you are provided with two sets, A and B. Your task is to determine if set A is a subset of set B.

T = int(input())
for _ in range(T):
    _ = int(input())
    setA = set(map(int, input().split()))
    _ = int(input())
    setB = set(map(int, input().split()))
    print(setA.issubset(setB))
