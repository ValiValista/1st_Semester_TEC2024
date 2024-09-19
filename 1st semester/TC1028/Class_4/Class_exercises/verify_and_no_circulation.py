"""
E. Velazquez A01647566

inputs: 
    placas
outputs:
    status
"""

menu = int(input("What would you like to do \n 1. Check verification status \n 2. Check circulation status \n 3. Exit \n Input type: 1,2,3: "))
if menu==1:
    print("This program takes the last number of your plates and returns when it has to be verified")
    placas = int(input("Insert the last number on your plates 0-9: \n"))
    if placas ==1 or placas ==2:
        print("You have to verify this Jan-Feb")
       
    elif placas == 3 or placas ==4:
        print("You have to verify this Mar-Apr")
       
    elif placas ==5 or placas ==6:
        print("You have to verify this May-Jun")
       
    elif placas ==7 or placas ==8:  
        print("You have to verify this Jun-Sep")
       
    elif placas ==9 or placas ==0:
        print("You have to verify this Oct-Nov")
       
    else:
        print("Error, try again.")

elif menu==2: 
    print("This program takes the last number of your plates and returns on what days it can be driven")
    placas = int(input("Insert the last number on your plates 0-9: "))
    if placas ==1 or placas ==2:
        print("You cannot drive thursdays")
       
    elif placas ==3 or placas ==4:
        print("You cannot drive wednesdays")
       
    elif placas ==5 or placas ==6:
        print("You cannot drive mondays")
       
    elif placas ==7 or placas ==8:  
        print("You cannot drive tuesdays")
       
    elif placas ==0 or placas ==9:
        print("You cannot drive fridays")
       
    else:
        print("Error, try again.")
else:
   exit()


    