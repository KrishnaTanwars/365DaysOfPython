
# Ques : Given two timestamps (with time zones) for multiple test cases, calculate the absolute difference between them in seconds.

from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    t1_dt = datetime.strptime(t1, fmt)
    t2_dt = datetime.strptime(t2, fmt)
    return str(abs(int((t1_dt - t2_dt).total_seconds())))

if _name_ == '_main_':
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))