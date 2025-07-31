# 📌 Question: You are given n strings. For each string, check whether it is a valid regex pattern using Python.

# ✅ Valid Regex Checker
import re
import sys

data = sys.stdin.read().splitlines()
n = int(data[0])

for i in range(1, n + 1):
    pattern = data[i]
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")