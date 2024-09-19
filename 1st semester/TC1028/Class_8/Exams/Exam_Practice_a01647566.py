"""
Problem guideline:
    Loop so that you can add multiple packages
    Display price per package
    Sum all prices, print on end
    End on negative


Inputs: Peso del paquete en kilos

Process Variables:

Process Constants:
    <10kg = 200
    =>10kg <45kg = 700 + 55 per kilo above 10
    =>45kg <90kg = 1000 + 65 per kilo above 45
    =>90 = 1500 + 75 per kilo above 90

Outputs: Costo por la transportacion


Don't forget!
    Check if greater than 0
    Convert to int, float, str, in their respective circumstances
    Put everything into functions and call them in main

        If menus are used: used While True: and sys.exit()


"""
import sys

def fun_package_price(func_kg):
    if func_kg >0:
        if func_kg < 10:
            func_price = 200
            return func_price
        elif 10 <= func_kg < 45:
            func_price = 700 + (55 * (func_kg-10))
            return func_price
        elif 45 <= func_kg < 90:
            func_price = 1000 + (65 * (func_kg-45))
            return func_price
        elif 90 <= func_kg < 150:
            func_price = 1500 + (75 * (func_kg-90))
            return func_price
        else:
            print("Error")
            main()

def main():
    sum_of_packages = 0
    while True:
        kg = float(input("Enter Kg: "))
        if kg>0:
            sum_of_packages = sum_of_packages + fun_package_price(kg)
            print(f"Price for this package is {fun_package_price(kg)}")
        elif kg <0:
            print(f"The sum of the packages is {sum_of_packages}")
            sys.exit("Done")



main()