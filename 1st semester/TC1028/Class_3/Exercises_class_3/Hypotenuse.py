"""
Exercise 1

Write a program that calculates the opposite side length of a right triangle whose hypotenuse is given by the user and has a base angle of 30°

Use the formula:

sin θ = opposite side / hypotenuse
"""

import math
hip=float(input("hipotenuse: "))
opp=(math.sin(math.radians(30))*hip)
print(f"Side lenght {opp:.2f}")

