# ✅ Q2: Safe Integer Division
# Input:

# First line: number of test cases T

# Next T lines: two space-separated values a and b

# Output:

# Print a // b

# If error, print: Error Code: <error_message>

for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)