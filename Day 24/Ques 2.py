# Problem: Given two timestamps with timezones, find absolute difference in seconds.

from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    return str(abs(int((dt1 - dt2).total_seconds())))

t = int(input())
for _ in range(t):
    t1 = input().strip()
    t2 = input().strip()
    print(time_delta(t1, t2))