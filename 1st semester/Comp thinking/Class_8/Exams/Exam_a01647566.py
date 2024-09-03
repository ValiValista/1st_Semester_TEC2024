"""
Made by Vasco: A01647566

Problem guideline:
HABITTATE is a creative company where architects and engineers make construction or remodeling proposals to their
clients and have asked you to develop a simple system where the user can have a pre-quote depending on the type of finishes
and the square meters of construction.

The square meter of remodeling costs $2,000.00 pesos,
the construction costs $4,000.00 pesos and they want to propose two
parameters: normal finish, or luxury finish.
For "luxury finishing" you will have to increase the price per square meter in
remodeling by 15% and 30% in square meter for construction.
If construction of more than 250 mts^2 in luxury finish is quoted, the design of the gardens is given away.



>Habittate Menu
1. Construction project quote
2. Play for a promotion
3. Exit



Inputs:
    Cotization, raffle, exit menu choice
    Remodelation or construction choice
    Choice normal or luxury finish
    Square meter of the chosen finish

Process Variables:

Process Constants:
    Square meter of remodeling = 2000

Outputs:
    Price for the total construction


Don't forget!
    Check if greater than 0
    Convert to int, float, str, in their respective circumstances
    Put everything into functions and call them in main
        If menus are used: used While True: and sys.exit()

"""
from sys import exit
from time import sleep
from random import randint

def error(): #This function handles errors by throwing you back into the main menu :P
    print("Error handled")
    sleep(1)
    main()

#All this functions are not entirely required and could be made redundant by fixing the boolean logic on lines 107-118
#In reality this is only to prove I know how to use functions
def fun_remodel_normal(fun_sqr_mtr):
    fun1_f_price = fun_sqr_mtr * 2000
    return fun1_f_price
def fun_remodel_luxury(fun_sqr_mtr):
    fun2_f_price = fun_sqr_mtr * (2000 + 2000 * .15)
    return fun2_f_price
def fun_construct_normal(fun_sqr_mtr):
    fun3_f_price = fun_sqr_mtr * 4000
    return fun3_f_price
def fun_construct_luxury(fun_sqr_mtr):
    fun4_f_price = fun_sqr_mtr * (4000 + 4000 * .30)
    return fun4_f_price

def fun_cotiza(): #This function handles the first menu option
    key_men_cotiza = int(input(""" 
Do you want to.
1. Remodel
2. Construct 
"""))
    # Menu for remodelling
    if key_men_cotiza == 1:
        type_o_finish = int(input("""
Choose the finish you want to have.
1. Normal 
2. Luxury
"""))
        sqr_mtr = fun_type_o_finish(type_o_finish)
        if sqr_mtr > 0:
            if type_o_finish == 1:
                f_price = fun_remodel_normal(sqr_mtr)
                print(f"Your total would be ${f_price:,.2f}")
                sleep(1)
            elif type_o_finish == 2:
                f_price = fun_remodel_luxury(sqr_mtr)
                print(f"Your total would be ${f_price:,.2f}")
                sleep(1)
            else:
                error()
        else:
            error()

    # Menu for construction
    elif key_men_cotiza == 2:
        type_o_finish = int(input("""
Choose the finish you want to have.
1. Normal 
2. Luxury
"""))
        sqr_mtr = fun_type_o_finish(type_o_finish)
        #Comprobation of greater than 0, not greater than 1 cause square meters could be 0.1
        if 0 < sqr_mtr < 250:
            if type_o_finish == 1:
                f_price = fun_construct_normal(sqr_mtr)
                print(f"Your total would be ${f_price:,.2f}")
                sleep(1)
            elif type_o_finish == 2:
                f_price = fun_construct_luxury(sqr_mtr)
                print(f"Your total would be ${f_price:,.2f}")
                sleep(1)
            else:
                error()
        elif sqr_mtr >=250:
            # If greater than 250 check if it is luxury finish
            # Could probably do it some other way more efficiently, a little short on time
            if type_o_finish == 1:
                f_price = fun_construct_normal(sqr_mtr)
                print(f"Your total would be ${f_price:,.2f}")
                sleep(1)
            elif type_o_finish == 2:
                f_price = fun_construct_luxury(sqr_mtr)
                print(f"Your total would be ${f_price:,.2f} and Congratulations, you will get a free design on your garden")
                sleep(1)
            else:
                error()
        else:
            error()

    else:
        error()

def fun_type_o_finish(func_var_type_o_finish):
    if func_var_type_o_finish == 1:
        sqr_meters_normal = float(input("Enter square meter of normal finish: "))
        return sqr_meters_normal
    elif func_var_type_o_finish == 2:
        sqr_meters_luxury = float(input("Enter square meter of luxury finish: "))
        return sqr_meters_luxury
    else:
        print("Error unknown finish type")
        sleep(1)
        error()

def fun_raffle():
    print(f"You have won a {randint(10,20)}% discount if you choose to hire our services today")
    sleep(1)

def main():

    while True:
        key_men_main = int(input("""
Please enter a menu option from the following:
1. Construction project quote
2. Raffle
3. Exit    
"""))
        if key_men_main == 1:
            fun_cotiza()
        elif key_men_main == 2:
            fun_raffle()
        elif key_men_main == 3:
            exit("Thank you for choosing us!")
        else:
            error()
main()

