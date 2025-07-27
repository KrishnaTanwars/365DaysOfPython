# -------------------------------------------
# 📌 Problem 1: Average of Distinct Heights
# -------------------------------------------

# Description:
# Given a list of plant heights (possibly with duplicates),
# calculate the average of only the distinct heights.
# Round the result to 3 decimal places.

def average(array):
    unique_heights = set(array)
    avg = sum(unique_heights) / len(unique_heights)
    return round(avg, 3)

if __name__ == '__main__':
    print("🔹 Problem 1: Average of Distinct Heights 🔹")
    n = int(input("Enter number of plants: "))
    arr = list(map(int, input("Enter plant heights separated by space: ").split()))
    result = average(arr)
    print("Average of distinct heights (rounded to 3 decimal places):", result)
