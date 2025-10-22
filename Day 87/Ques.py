# Ques : Find the runner-up score from a list of integers.

n = int(input())
arr = list(map(int, input().split()))
print(sorted(set(arr))[-2])
