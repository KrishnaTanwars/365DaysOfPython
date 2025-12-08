# Ques : Calculate final happiness by adding +1 for array elements in set A and −1 for elements in set B.

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = sum((1 if x in A else -1 if x in B else 0) for x in arr)
print(happiness)
