

new_gift_card_amount = 1000 #Integer defined as 1000 currency value
commission_credit_card = 6 #Percentage = 6%
discount_giftcard = 10 #Percentage = 10%
reward_amount_on_giftcard = 700 #The required purchase amount to earn a free ice cream when the purchase is done thru gift card

def valid_input(prompt):
    while True:
        try:
            answer = int(input(prompt))
            if answer >= 0:
                return answer
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def menu_adult():
    print("""
Our menu for the day is:
1.   Pasta: 25 pesos 
2.   Sandwich: 20 pesos 
3.   Carlos V: 5 pesos
4.   Water: 1 peso for the cup
Please enter an amount per product, leave as 0 if you do not intend to buy that product
""")

def menu_child():
    pass

def payment_process():
    pass

def recharge_giftcard():
    pass

def auth_giftcard():
    pass

def purchase_menu():
    pass

def main_menu():
    menu_adult_selection = []
    key_men = valid_input("""
Please input a menu option:

1. Comida para adultos
2. Menú de niños
3. Realizar Pago
4. Abono a Tarjeta de Prepago
5. Salir         

""")

    if key_men == 1:
        menu_adult_selection = menu_adult([])

    elif key_men == 2:
        menu_child()

    elif key_men == 3:
        payment_process(menu_adult_selection)

    elif key_men == 4:
        auth_giftcard()
        recharge_giftcard()

    elif key_men == 5:
        exit(420)

    else:
        pass




def main():
    main_menu()

main()
