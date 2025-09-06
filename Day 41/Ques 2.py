# Question: You are given a string consisting of digits, commas (,), and dots (.). Your task is to split the string at every comma and dot.

import re

regex_pattern = r"[,.]"

print("\n".join(re.split(regex_pattern, input())))