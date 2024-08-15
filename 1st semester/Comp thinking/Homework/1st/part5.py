"""
Made by Viri V. #A01647566
Problem: Calculate the hipotenuse of a right side triangle from 2 sides
Input: 
    2 sides
Output: 
    hipotenuse
"""
import math #imports the math library from python for use exclusively in the sqrt 

print("\nThis program takes 2 sides from a triangle and spits out the hipotenuse\n") #Instructions

cat_a = float(input("Insert the first side in cm: ")) #first side input
cat_b = float(input("Insert the second side in cm:  ")) #second side input

hip = (math.sqrt((cat_a**2) + (cat_b**2))) #Pythagorean theorem

print(f"\nThe triangle's hipotenuse is {hip:.3f}cm\n")