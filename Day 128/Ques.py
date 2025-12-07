# Ques : Find angle MBC (in degrees, rounded) in a right triangle given sides AB and BC, where M is midpoint of hypotenuse AC.

import math

AB = int(input())
BC = int(input())

angle = round(math.degrees(math.atan(AB/BC)))
print(angle)
