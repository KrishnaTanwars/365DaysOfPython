# Ques : Given multiple lines of code, replace only those && and || that have spaces on both sides.
# Convert && → and and || → or, keeping surrounding spaces intact.

import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        line = input()
        line = re.sub(r'(?<= )&&(?= )', 'and', line)
        line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
        print(line)
