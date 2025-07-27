
# -------------------------------------------
# 📌 Problem 2: DefaultDict Group Match
# -------------------------------------------

# Description:
# You're given n words in group A and m query words in group B.
# For each query word, print the 1-based indices of its occurrences in group A.
# If a word doesn't exist in group A, print -1.

from collections import defaultdict

def defaultdict_problem():
    print("\n🔹 Problem 2: DefaultDict Group Match 🔹")
    n, m = map(int, input("Enter n and m: ").split())

    group_a = defaultdict(list)

    print("Enter words for group A:")
    for i in range(1, n + 1):
        word = input()
        group_a[word].append(i)

    print("Enter words for group B:")
    for _ in range(m):
        query = input()
        if query in group_a:
            print(' '.join(map(str, group_a[query])))
        else:
            print(-1)

# Uncomment the following line to run Problem 2 in the same session
# defaultdict_problem()
