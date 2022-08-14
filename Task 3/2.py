from math import acos
from math import degrees
from math import sqrt


# taking the length of two sides
AB = int(input())
BC = int(input())
hypo = sqrt(AB**2+BC**2) # val of hypotenuse
angle = acos(BC/hypo ) # value of angle
print(str(round(degrees(angle)))+u"\N{DEGREE SIGN}")