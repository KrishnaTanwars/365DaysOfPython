# Question: The re.sub() tool evaluates a pattern and, for each valid match, calls a method (or lambda). The method is called for all matches and can be used to modify strings in different ways. The problem shows an example of using re.sub() to square numbers in a string.

import re

def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
