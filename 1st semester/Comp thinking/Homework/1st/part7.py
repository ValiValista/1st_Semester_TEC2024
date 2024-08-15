"""
Made by Viri V. #A01647566
Problem: Calculate the hipotenuse from a given side and angle
Input: 
    Side and angle
Output: 
    Hipotenuse
"""

import math #imports the math library from python for use exclusively in the sqrt 

print("\nThis program takes the opposite side of a triangle and its angle and spits out the hipotenuse\n") #Instructions

cat_a = float(input("Insert the side in cm: ")) #first side input
angle_d = float(input("Insert the angle in degress:  ")) #angle input in degrees
hip = float(cat_a / math.sin(math.radians(angle_d))) #gets the hipotenuse based on the sin of the opposite side 


print(f"\nThe triangle's hipotenuse is {hip:.3f}cm\n")
#print(f"{cat_b}, {angle_d}") #debug