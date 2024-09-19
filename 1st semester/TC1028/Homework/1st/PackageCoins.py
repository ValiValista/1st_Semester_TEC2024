"""
Made by Viri V. #A01647566
Problem: Take a total number of coins, calculates the least amount of bills of amounts 200, 50, 20 they fit in 
Input: 
    total number of coins
Output: 
    Bills and remainder
"""

# Program guidelines
print("\nThis program will ask your for an amount of 1 peso coins, and will give you the bills you would give in exchange and the remainder\n")

t_coins = int(input("Please insert a number of 1 peso coins: "))

# divide by 200, get remainder, divide that by 50, get remainder, divide that by 20, get remainder, print all results

pack1 = t_coins//200 #Store the amount of coins that fit in boxes of 200 as a whole number
rem1 = t_coins%200 #Store the remainder for future calculations

pack2 = rem1//50 #Take the remainder from the previous operations, then divides it by 50 and returns a whole number
rem2 = rem1%50 #Store the remainder for future calculations

pack3 = rem2//20 #Take the remainder from the previous operations, then divides it by 20 and returns a whole number
rem3 = rem2%20 #Store the remainder for output as a final remainder

print(f"\n{t_coins} 1 peso coins is equivalent to: {pack1:.0f} 200MXN bills, {pack2:.0f} 50MXN bills, {pack3:.0f} 20MXN bills, \nand there is {rem3:.0f} pesos in loose change \n")
#print(f"Remainders are {rem1}, {rem2}") #For debugging purposes, remove first #


