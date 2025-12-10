# Ques : Print the top three most common characters in a string, sorted by frequency desc and alphabetically for ties.

from collections import Counter

s = input().strip()
cnt = Counter(s)

for ch, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(ch, c)
