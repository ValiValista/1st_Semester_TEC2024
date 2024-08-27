# Made by Vasco A01647566

#Libraries

#Function definition
def addition(func_num_1_add, func_num_2_add):
    func_num_added = func_num_1_add + func_num_2_add
    return  func_num_added

def substraction(func_num_1_sub, func_num_2_sub):
    func_num_subs = func_num_1_sub - func_num_2_sub
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

#main
def main():
    #main loop
    while True: 

        num1 = float(input("\nInput first number: ")) 
        num2 = float(input("Input second number: "))
                
        print("""
        Welcome to the calculator app please select an operation:
        a. Addition
        s. Substraction
        m. Multiplication
        d. Division
        e. Exponentiation
        """)
        menu_in_calc = input(f"\n")
        
        if menu_in_calc == "a":
            num_added = addition(num1, num2)
            print(f"\n{num1} + {num2} = {num_added}")
            
        elif menu_in_calc == "s":
            num_subs = substraction(num1, num2)
            print(f"\n{num1} - {num2} = {num_subs}")
            
        elif menu_in_calc == "m":
            num_mult = multiplication(num1, num2)
            print(f"\n{num1} * {num2} = {num_mult}")
            
        elif menu_in_calc == "d":
            num_div = division(num1, num2)
            print(f"\n{num1} / {num2} = {num_div}")
        
        elif menu_in_calc == "e":
            num_exp = exponentiation(num1, num2)
            print(f"\n{num1} ** {num2} = {num_exp}")

        elif menu_in_calc == "na":
            break
            
        else:
            print("Error")

main()