"""
Challenge N.1:
    Age.
    Depending on the age that the user inserts you classify them as 
    baby, child, teen, young, adult, adult, old adult, corpse, mummy, dust



Inputs: 
    Age
Outputs:
    Classification

Process:

"""
age = float(input("What is your age: "))

if age <=5: 
    print("You are a baby")

elif age <=11:
    print("You are a child")

elif age <=17:
    print("You are a teen")
    
elif age <=27:
    print("You are a young adult")

elif age <=59:
    print("You are an adult")
    
elif age <=89:
    print("You are an elder")

elif age <=99:
    print("You are a marvel")
    
elif age >99:
    print("You are a mummy")

else:
    print("You are a ERROR 404")

