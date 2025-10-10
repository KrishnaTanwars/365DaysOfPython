# Ques : Calculate the absolute time difference in seconds between two given timestamps that include time zone information (format: Day dd Mon yyyy hh:mm:ss +xxxx).

from datetime import datetime
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    t1_dt = datetime.strptime(t1, fmt)
    t2_dt = datetime.strptime(t2, fmt)
    return str(abs(int((t1_dt - t2_dt).total_seconds())))
