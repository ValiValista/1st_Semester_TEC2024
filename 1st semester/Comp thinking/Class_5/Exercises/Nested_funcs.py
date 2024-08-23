# Made by Vasco A01647566

#Libraries
import math
import random

def main():
    while True:
        def addition(func_num_1_add, func_num_2_add):
            func_num_added = func_num_1_add + func_num_2_add
            return  func_num_added
    
        def substraction(func_num_1_sub, func_num_2_sub):
            func_num_subs = func_num_1_sub + func_num_2_sub
            return  func_num_subs
        
        def multiplication(func_num_1_mult, func_num_2_mult):
            func_num_mult = func_num_1_mult * func_num_2_mult
            return  func_num_mult
        
        def division(func_num_1_div, func_num_2_div):
            func_num_div = func_num_1_div / func_num_2_div
            return  func_num_div
                 
        def exponentiation(func_num_1_exp, func_num_2_exp):
            func_num_exp = func_num_1_exp ** func_num_2_exp
            return  func_num_exp
        
        def sqrt(func_num_1_sqrt):
            func_num_sqrt = math.sqrt(func_num_1_sqrt)
            return  func_num_sqrt
            
        print("""
            Press 1 to launch calculator
            Press 2 to launch Hello World
            Press 3 to launch hell in earth
            Press 4 to Exit
            """)

        
        menu_in_main = int(input())
        if menu_in_main == 1:
            
            print("""
            Welcome to the calculator app please select an operation:
            1. Addition
            2. Substraction
            3. Multiplication
            4. Division
            5. Exponentiation
            6. Square root
            """)
            
            menu_in_calc = int(input())
            
            if menu_in_calc == 1:
                add_num1 = float(input("Input first number: "))
                add_num2 = float(input("Input second number: "))
                num_added = addition(add_num1, add_num2)
                print(f"{add_num1} + {add_num2} = {num_added}")
                
            elif menu_in_calc == 2:
                sub_num1 = float(input("Input first number: "))
                sub_num2 = float(input("Input second number: "))
                num_subs = substraction(sub_num1, sub_num2)
                print(f"{sub_num1} - {sub_num2} = {num_subs}")
                
            elif menu_in_calc == 3:
                mult_num1 = float(input("Input first number: "))
                mult_num2 = float(input("Input second number: "))
                num_mult = multiplication(mult_num1, mult_num2)
                print(f"{mult_num1} * {mult_num2} = {num_mult}")
                
            elif menu_in_calc == 4:
                div_num1 = float(input("Input first number: "))
                div_num2 = float(input("Input second number:"))
                num_div = division(div_num1, div_num2)
                print(f"{div_num1} / {div_num2} = {num_div}")
            

            elif menu_in_calc == 5:
                exp_num1 = float(input("Input first number: "))
                exp_num2 = float(input("Input second number:"))
                num_exp = exponentiation(exp_num1, exp_num2)
                print(f"{exp_num1} ** {exp_num2} = {num_exp}")
            
            elif menu_in_calc == 6:
                sqrt_num1 = float(input("Input number: "))
                num_sqrt = sqrt(sqrt_num1)
                print(f"Square of {sqrt_num1} = {num_sqrt}")
                
            else:
                print("Error")

            
        elif menu_in_main == 2:
            print("\nHello World\n")   
            
        elif menu_in_main == 3:
            print("\nUnavailable, earth is beauty\n")

        elif menu_in_main == 4:
            break
        
        else:
            print("Error")

            

main()