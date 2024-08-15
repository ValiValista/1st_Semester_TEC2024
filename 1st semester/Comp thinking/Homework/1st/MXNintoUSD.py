""" 
Made by Viri V. #A01647566
Problem: Doing a MXN to USD convertion with user inputted data

Inputs:
    Amount of currency | in_Cur
    Exchange rate of currency | ex_Cur

Outputs:
    Output Currency | out_Cur

"""

# Would love to use an API to do this but I assume that is outside the scope of the homework


print("\nThis program will take a given amount of pesos and the current exchange rate and then will output the amount in usd\n")
# Inputting
in_Cur = float(input("Please insert an amount of pesos to convert: "))
ex_Cur = float(input("Please insert the current exchange rate from pesos to dollars: Ej. 17.2 pesos per dollar:  "))

# Exchange process
out_Cur = in_Cur/ex_Cur #just divides the currency by the exchange rate to get the dollar amount

# Outputting
print(f"\nThat would be {out_Cur:.2f} dollars at the current exchange rate\n")