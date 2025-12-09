# Ques : Count occurrences of each word and print counts in order of first appearance.

from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    w = input().strip()
    d[w] = d.get(w, 0) + 1

print(len(d))
print(*d.values())
