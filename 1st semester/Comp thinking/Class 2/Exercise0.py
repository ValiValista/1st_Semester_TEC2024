"""
This algorythm calculates the given tip for a given bill

Inputs: 
    bill_Brute
    tip_Input
    tip_Percentage
Outputs: 
    real_Tip
    bill_WTip

    
Step 1. Print what the program does to the user
Step 2. Ask the user for the meal price without the tip 
Step 2.1 Store it in a variable bill_Brute
Step 3. Ask for the percentage of tip to give 
Step 3.1 Store it in a variable tip_Input
Step 4. Divide the tip_Percentage by 100
Step 4.1 Store that in tip_Percentage
Step 5. Multiply the meal price times the tip percentage 
Step 5.1 Store this as a variable real_Tip
Step 6. Sum the meal price and the tip 
Step 6.1 Store this in a variable call it bill_WTip
Step 7. Print the bill_WTip and real_Tip
"""



print("This program takes a given percentage written as an integer, and a bill amount, does math and gives you the tip, and the bill with the tip included")
bill_Brute = input(("What is your bill amount without a tip included: "))
tip_Percentage = input(("What is the amount of tip you want to give? Ej. 5, 10, 15, 20, 25: "))/100
tip_Total = bill_Brute * tip_Percentage 
bill_Total = bill_Brute + tip_Total
print(f"Your bill total with a tip is {bill_Total}, and your tip is {tip_Total}") 



