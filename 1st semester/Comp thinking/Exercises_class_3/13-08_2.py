"""
The area and volume of a sphere is calculated with the following formulas:

area =  LaTeX: 4\pi r^24πr2

volume = LaTeX: \frac{4\pi r^3}{3}4πr33

Write a program that asks for the value of the radius and displays its area and volume.
"""

# Libraries
import math

# Inputs
print("This program calculates the area and volume of any given radius from a circle or sphere")

radius=float(input("Input your radius: "))
# Operands
area=(4*math.pi*(radius**2))

volume=(4*math.pi*radius**3)/3

# Output
print(f"And sphere of radius {radius}, has an area of {area:.4f}², and volume of {volume:.4f}³")

