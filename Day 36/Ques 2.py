# Question: You are given a matrix of characters. Decode the script by reading the matrix column by column and then replacing any non-alphanumeric symbol sequences that are between two alphanumeric characters with a single space.

import re

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Read the matrix column by column to form the decoded string
decoded = "".join([matrix[j][i] for i in range(m) for j in range(n)])

# Use regex to substitute symbol sequences between alphanumeric characters with a space
decoded = re.sub(r'(?<=\w)[!@#$%& ]+(?=\w)', ' ', decoded)

print(decoded)