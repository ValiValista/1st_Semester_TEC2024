"""
E. Velazquez A01647566

Challenge N.1:
    Age.
    Depending on the age that the user inserts you classify them as 
    baby, child, teen, young, adult, adult, old adult, corpse, mummy, dust

This program takes scores on exams and project and outputs a pass fail status


Inputs: 
    score
Outputs:
    Classification

Process:

"""
print("This program takes scores on exams and project and outputs a pass fail status")
age = float(input("What is your score in the exam: "))
age2 = float(input("What is your score in the project: "))

if age and age2 >=80: 
    print("You pass")

elif age >= 70 and age2 >=50 :
    print("You are on CONDITIONAL STATUS")

else:
    print("You are DEAD")

