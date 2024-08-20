"""
E. Velazquez A01647566

Quadratic formula
 ax²+bx+c = 0
 x = (-b+sqrt(b²-4ac))/2
"""

import math
print("program does a quadractic equation by general formula")
a = float(input("Input a:"))
b = float(input("Input b:"))
c = float(input("Input c:"))

# Calculate the root
root = b**2 - 4*a*c
    
# Check if the root is negative, positive or zero
if root > 0:
    root1 = (-b + math.sqrt(root)) / (2*a)
    root2 = (-b - math.sqrt(root)) / (2*a)
    print(f"The equation has two real and distinct roots: {root1} and {root2}")
elif root == 0:
    root = -b / (2*a)
    print (f"The equation has one real and repeated root: {root}")
else:
    print("Error")