
# Ques : You are given n words that may repeat — count how many distinct words there are and how many times each appears.
# Print the number of unique words and their occurrence counts in input order.

from collections import OrderedDict

n = int(input())
counter = OrderedDict()

for _ in range(n):
    w = input().strip()
    counter[w] = counter.get(w, 0) + 1

print(len(counter))
print(" ".join(map(str, counter.values())))