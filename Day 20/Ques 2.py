# Question: Given a set and several other sets, perform mutation operations (update, intersection_update, difference_update, symmetric_difference_update) on the main set. Output the sum of the final elements in the set.


_ = int(input())
A = set(map(int, input().split()))
for _ in range(int(input())):
    op, _ = input().split()
    getattr(A, op)(set(map(int, input().split())))
print(sum(A))
