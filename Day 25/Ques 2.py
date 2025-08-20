# Question: You are given n words. Output the number of distinct words. Then, on the next line, output the number of occurrences for each distinct word, in the order of their first appearance.

from collections import OrderedDict

n = int(input().strip())
word_count = OrderedDict()

for _ in range(n):
    word = input().strip()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(*word_count.values())