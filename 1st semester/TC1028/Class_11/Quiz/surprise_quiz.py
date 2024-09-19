"""



"""
def get_valid_input(prompt):
    while True:
        try:
            answer = int(input(prompt))
            if answer >= 0:
                return answer
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def km_to_mile():
    km_max = get_valid_input("Please input a number to define the cap: ")+1
    print("KM \t \t Miles")
    for kilometers in range(km_max):
        miles_amount = kilometers * 0.62137
        print(f"{kilometers} \t \t {miles_amount:.2f}")

def meters_to_yard():
    meters_max = get_valid_input("Please input a number to define the cap: ")+1
    print("Meters \t \t Yards")
    for meters in range(meters_max):
        yards = meters * 1.0936133
        print(f"{meters} \t \t {yards:.2f}")
def main():

    while True:
        print("""
This program does metric to imperial conversion from kilometers and meters to miles and yards
1. kilometers to miles,
2. meters to yards,
3. Exit
        """)
        men_key = get_valid_input("Please input a menu option: ")
        if men_key == 1:
            km_to_mile()
        elif men_key == 2:
            meters_to_yard()
        elif men_key == 3:
            print("Thanks")
            break
        else:
            pass
    
main()