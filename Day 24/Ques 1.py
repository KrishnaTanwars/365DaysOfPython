# Problem: Right triangle △ABC, right angle at C, sides AC=b, BC=c, find angle θ at B.

import math

b = float(input())
c = float(input())

theta_deg = round(math.degrees(math.acos(c / math.sqrt(b**2 + c**2))))
print(f"{theta_deg}\u00B0")