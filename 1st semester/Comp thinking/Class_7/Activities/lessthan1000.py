#A01647566
def main():
    suma = 0
    counter = 0
    while suma <= 1000:
        a = int(input("\nInput a number: "))
        suma += a
        print(f"\nYou've added {counter} numbers")
        counter += 1
        
    print(f"\nThe sum is {suma}")    

main()