# ✅ Q1: Print Day of the Week
# Input: A single line with 3 integers: MM DD YYYY
# Output: Day of the week in uppercase (e.g., WEDNESDAY)


import calendar

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
