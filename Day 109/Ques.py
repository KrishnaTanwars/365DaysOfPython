# Ques : Given a lowercase string, find the three most common characters and their frequencies.
# Print them in descending order of count, and alphabetically if counts are equal.

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