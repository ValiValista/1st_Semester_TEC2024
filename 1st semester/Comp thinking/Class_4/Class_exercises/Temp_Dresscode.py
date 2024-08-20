"""
E. Velazquez A01647566


Inputs: temperature

Outputs: dress code

this program takes a given temperature and gives you a proper dress code for the weather

"""
print("this program takes a given temperature and gives you a proper dress code for the weather")
temp = float(input("What is the temperature outside: "))

if temp >= 30:
    print("Sleevesless shirt and shorts")
elif temp <30 and temp >15:
    print("t-shirt and jeans")
elif temp <0:
    print("Trench coat and heaters")
else:
    print("Sweater and pants")