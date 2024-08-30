

def is_perfect():
        
    number = int(input("Input number: "))
    counter = 1
    sum = 0
    
    while counter < number:
        if number % counter == 0:
            sum += counter
        counter += 1
    
    if number == sum:
        print("Perfection")
    else:
        print("Error")
def main():
    is_perfect()
main()    
