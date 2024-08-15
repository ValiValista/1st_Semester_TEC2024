"""
Made by Viri V. #A01647566
Problem: Calculate the area of a tetrahedon
Input: 
    side of a face
Output: 
    Area³
"""

#It occurs to me I could also select the way to obtain result
#Meaning I could also make it obtain the area from another input, such as height or volume, but that is outside the scope for now


# Libraries
import math

# Inputs
print("\nThis program calculates the area of any tetrahedon from its edge lenght. \n")

lenght=float(input("Input edge lenght in cm: "))


# Operands
area_cubed=((lenght**2)*math.sqrt(3))


# Output
print(f"\nThat tetrahedron has an area of {area_cubed:.3f}cm³\n")
