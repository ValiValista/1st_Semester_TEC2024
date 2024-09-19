"""
Made by Viri V. #A01647566
Problem: This program calculates a person's BMI based on the two given inputs of weight and height
Formula: BMI = weight/height²
Inputs:
    Weight
    Height
Outputs: 
    BMI
"""

# Instructions and inputs
print("\nThis program will take a given height and weight and give you the BMI for the corresponding person\n")
Weight = float(input("What is your weight in KG: "))
Height = float(input("What is your height in meters Ej. 1.80: "))

# Data processing
BMI = (Weight / (Height**2))


# Outputting
print(f"\nYour BMI is {BMI:.3f}\n")