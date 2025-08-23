
# Question: You are given a function f(X)=X2  and K lists. You have to pick one element from each list to maximize the value of S=(f(X_1)+f(X_2)+ dots+f(X_K)). Find the maximum value, S_max.

from itertools import product

k, m = map(int, input().split())
lists = []

for _ in range(k):
    data = list(map(int, input().split()))
    lists.append(data[1:])

all_combinations = product(*lists)

max_val = 0
for comb in all_combinations:
    val = sum(x**2 for x in comb) % m
    if val > max_val:
        max_val = val

print(max_val)
