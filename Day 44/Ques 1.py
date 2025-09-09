# Question: Given a list of rational numbers, find their product. Use the reduce() function.

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator