"""Problem Description:

Given N words as input, where some words may repeat.
Output two lines:

The total number of distinct words.

The number of occurrences for each distinct word, ordered by the word's appearance in the input."""



from collections import OrderedDict

n = int(input())
words = [input().strip() for _ in range(n)]
count = OrderedDict()

for word in words:
    # Use .get() to safely retrieve the current count, defaulting to 0, then increment
    count[word] = count.get(word, 0) + 1

# Line 1: Output the number of distinct words (length of the OrderedDict)
print(len(count))

# Line 2: Output the counts of the words, joined by a space
# Since OrderedDict maintains insertion order, the values are in the correct appearance order
print(' '.join(str(v) for v in count.values()))