"""
Made by Viri V. #A01647566
Problem. Calculate the area of a circle
Input: 
    Radius
Output: 
    Area
"""
# Libraries
import math

# Inputs
print("\nThis program calculates the area from any given radius from a circle. \n")

radius=float(input("Input your radius in cm: "))

# Operands
area=(math.pi*(radius**2))


# Output
print(f"\nA circle of radius of {radius}cm, has an area of {area:.3f}cm²\n")
