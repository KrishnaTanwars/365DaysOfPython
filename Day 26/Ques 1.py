# Question: Find the top three most common characters in a given string. Print each character and its count on a new line. Sort the output in descending order of the count. If the counts are the same, sort the characters alphabetically.

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    for ch, cnt in sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(ch, cnt)