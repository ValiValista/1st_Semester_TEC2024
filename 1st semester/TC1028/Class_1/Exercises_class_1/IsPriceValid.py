#Exercise 1

#Write an algorithm that verifies if a price given by the user is valid or not. To be a valid price, it must be a positive value (greater than zero)

print ("This program will check if the price inputted is a positive value")
price = float (input("Insert price: "))
if price > 0:
    #check = True # This part is completely unnecesary for the scale of the program, uncomment if you want to use it in a function or something
        print ("Price is a valid")
else:
    #check = False # This part is completely unnecesary for the scale of the program, uncomment if you want to use it in a function or something
    print ("Invalid price")
