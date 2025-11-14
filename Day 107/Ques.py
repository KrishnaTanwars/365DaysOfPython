# Ques : Given an array of integers and two disjoint sets A and B, increase happiness by +1 for elements in A and decrease by −1 for elements in B.

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