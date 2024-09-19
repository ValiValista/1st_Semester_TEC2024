'''
Video game

GameStore has video game sales, the new ones cost 1,000 and the used ones cost 350.

Write a program to calculate the purchase total.

Input:

Two integers, one in each row, the first is the number of new games and the second is the number of used games.

Output:

The total of the purchase

Example:

>>>2

>>>3

3050
'''

new_amount = float(input("How many new games are you buying today? "))
old_amount = float(input("How many old games are you buying today? "))
ur_total = (new_amount * 1000) + (old_amount * 350) 
print("your total is" + ur_total)