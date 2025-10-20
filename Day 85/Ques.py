# Ques : Given a string S and an integer k, print all possible k-length permutations of the string S in lexicographic (sorted) order, each on a new line.

from itertools import permutations
s, n = input().split()
for p in sorted(permutations(s, int(n))):
    print(''.join(p))