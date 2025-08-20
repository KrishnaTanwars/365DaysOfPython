# Question: You are given an array and two disjoint sets, A and B. Your initial happiness is 0. For each integer in the array, if it is in set A, you add 1 to your happiness. If it is in set B, you add -1. Calculate the final happiness.

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1
print(happiness)
