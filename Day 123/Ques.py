# Ques : Given a lowercase string s, find the top 3 most frequent characters.
# Sort by frequency (desc), and if equal, sort by alphabetical order.

from collections import Counter

s = input().strip()
for ch, cnt in sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(ch, cnt)
