"""
Made by Viri V. #A01647566
Problem: Take a total number of pencils, calculates the least amount of packages of 200, 50, 20 they fit in 
Input: 
    total number of pencils
Output: 
    Packages and remainder
"""

# Program guidelines
print("\nThis program will ask your for an amount of pencils, and will give you the packages they would use and the remainder\n")

t_Pencils = int(input("Please insert a number of pencils: "))

# divide by 200, get remainder, divide that by 50, get remainder, divide that by 20, get remainder, print all results

pack1 = t_Pencils//200 #Store the amount of pencils that fit in boxes of 200 as a whole number
rem1 = t_Pencils%200 #Store the remainder for future calculations

pack2 = rem1//50 #Take the remainder from the previous operations, then divides it by 50 and returns a whole number
rem2 = rem1%50 #Store the remainder for future calculations

pack3 = rem2//20 #Take the remainder from the previous operations, then divides it by 20 and returns a whole number
rem3 = rem2%20 #Store the remainder for output as a final remainder

print(f"\nThere would be {pack1} pencil packs of 200, {pack2} pencil packs of 50, {pack3} pencil packs of 20, \nand there are {rem3} pencils without boxes \n")
#print(f"Remainders are {rem1}, {rem2}") #For debugging purposes, remove first #


