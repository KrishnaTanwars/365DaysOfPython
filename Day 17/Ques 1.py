# 📌 Question: Given n country stamps, count how many distinct countries are in the collection.

# ✅ Count Distinct Country Stamps
n = int(input())
stamps = set()

for _ in range(n):
    country = input()
    stamps.add(country)

print(len(stamps))