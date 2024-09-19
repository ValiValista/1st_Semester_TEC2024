"""
Average of 4 subjects

In a university each student takes 4 subjects in the semester. Develop a program that receives the grade for each subject, calculates the average of the 4 subjects and displays it.

Input:

4 whole numbers representing the grades for the 4 subjects, one number on each row.

Output:

A decimal number corresponding to the average.
"""

num1 = float(input("What is your grade for subject a? : "))
num2 = float(input("What is your grade for subject b? : "))
num3 = float(input("What is your grade for subject c? : "))
num4 = float(input("What is your grade for subject d? : "))

average = float ((num1 + num2 + num3 + num4)/4)

print (f"your average is {average}")

