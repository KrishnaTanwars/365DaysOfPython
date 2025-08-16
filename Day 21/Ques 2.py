# Question: You are given a set A and n other sets. Your task is to determine if set A is a strict superset of all the other n sets. A strict superset must contain all elements of the other set and also have at least one element that the other set does not.

A = set(input().split())
n = int(input())

is_strict_superset = True
for _ in range(n):
    other = set(input().split())
    if not (A.issuperset(other) and A != other):
        is_strict_superset = False
        break

print(is_strict_superset)