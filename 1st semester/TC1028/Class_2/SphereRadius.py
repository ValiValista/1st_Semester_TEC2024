"""
Problem. Calculate the area and volume of a sphere.
Input. radius.
Output. Area, volume.
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
