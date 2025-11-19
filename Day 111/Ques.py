# Ques : Given a full name, capitalize the first letter of each word. If a word starts with a number (e.g., 12abc), leave it unchanged.

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    words = s.split(" ")
    result = []

    for w in words:
        if len(w) > 0 and w[0].isalpha():
            result.append(w.capitalize())
        else:
            result.append(w)
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
