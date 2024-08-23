from random import randint

print("This program takes the total price for your purchase and gives you a menu for payment options.\n")

purc_total = float(input("Please input the purchase total: "))
if purc_total >0:

    men_option_1 = int(input("""
                Please type the option for your purchase;
                1. Pay in interest free monthly payments.
                2. Enter a raffle to get a discount from 10 to 30 percent.
                Please enter an option: 
                """))
    if men_option_1 == 1:
        men_option_m_payments = int(input(f""" 
                Enter one of the following options
                1. 6 monthly payments of ${purc_total/6:,.2f}.
                2. 12 monthly payments of ${purc_total/12:,.2f}
                """))
        if men_option_m_payments == 1:
            print(f"Your monthly payment would end up being ${purc_total/6:,.2f}, for a total of ${purc_total:,.2f}")
            
        elif men_option_m_payments == 2:
            print(f"Your monthly payment would end up being ${purc_total/12:,.2f}, for a total of ${purc_total:,.2f}")
        else:
            print("Error unknown option")
        
    elif men_option_1 == 2:
        raffle_disc = randint(1,3)
        print(f""" 
            Welcome to the raffle!!! 
            
            Your original price was ${purc_total:,.2f}
            You have won a {raffle_disc*10:,.2f}% discount
            Thanks to this discount your purchases ends up as ${purc_total-purc_total*(raffle_disc/10):,.2f}  
            
            Congratulations!! 
            You saved ${purc_total*(raffle_disc/10):,.2f}
            """)
        
    else:
        print("Error unknown input")
else:
    print("Error unknown input")


