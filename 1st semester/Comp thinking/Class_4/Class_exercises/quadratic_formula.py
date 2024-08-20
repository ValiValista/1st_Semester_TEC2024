"""
Quadratic formula
 ax²+bx+c = 0
 x = (-b+sqrt(b²-4ac))/2
"""

import math
print("program does a quadractic equation by general formula")
a = int(input("Input a:"))
b = int(input("Input b:"))
c = int(input("Input c:"))
if a == 0 and b == 0:
    print("error")
elif a == 0 and b >0:
    x=-c/b
    print(f"x = {x}")
else:
    x = (-(b)+math.sqrt(b**2-4*a*c))/2
    print(f"x1 = {x}, x2= -{x}")
