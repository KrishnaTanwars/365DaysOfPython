# Ques :  Company Logo (Top 3 chars by freq/alphabet)
from collections import Counter
s=input()
for c,n in sorted(Counter(s).items(), key=lambda x:(-x[1],x[0]))[:3]:
    print(c,n)
