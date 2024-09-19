#A01647566
def sum():
    suma = 0
    counter = 1
    while suma <= 1000:
        a = int(input("\nInput a number: "))
        suma += a
        print(f"\nYou've added {counter} numbers")
        counter += 1
        
    print(f"\nThe sum is {suma}")    

def main():
    print(f"""
This program displays the total of the sum, and the number of quantities that were added.
""")
    sum()
main()
    