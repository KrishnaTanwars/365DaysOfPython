# Question: Given a space-separated list of integers, check if all integers are positive, and if so, check if any integer is a palindromic integer.

n, nums = int(input()), input().split()
print(all(int(x) > 0 for x in nums) and any(x == x[::-1] for x in nums)