# Given a string S and an integer K, print all possible permutations of size K in lexicographic order

from itertools import permutations

# Input example: HACK 2
S, K = input("Enter string and permutation size (e.g., HACK 2): ").split()
K = int(K)

# Generate and sort permutations
perm_list = permutations(sorted(S), K)

# Print each permutation
print("\nAll lexicographic permutations:")
for p in perm_list:
    print(''.join(p))
