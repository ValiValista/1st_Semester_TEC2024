"""

Section comments:
This are defined by 3 quotations marks at the start line and the end line.
You can write all the text you want inside as a comment.

"""


"""
Problem: Calculate the price of a bag of oranges.


Inputs:
    price_kilos
    amount_kilos
Outputs:
    total
Process: Obtain the inputs via prompting, multiply the inputs, display result

"""


print("This program calculates price per kilogram of oranges")
price_kilos = float (input("Enter the price per kilo of oranges: $ "))
amount_kilos = float (input("Enter kilograms amount of the oranges: " ))
total = price_kilos * amount_kilos
print (f"Your total is {total}") #could also be written as: print("Your total is"+total) 
