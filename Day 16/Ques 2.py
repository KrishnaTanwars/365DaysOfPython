# 🧾 Question: Given two sets of integers, print their symmetric difference in ascending order.

# 💻 Code:

a = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

for num in sorted(A.symmetric_difference(B)):
    print(num)