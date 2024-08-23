def main():
    menu1 = int(input("""
                    Input menu
                    1. Happy birthday
                    2. Calculator
                    3. Undef
                    
                    """))
    if menu1 == 1:
        name = input("Input your name: ")
        age = int(input("Input your age: "))

        def happy_Birthday(x, y):
            print(f"Happy birthday {x} you are {y} now!")
            z = y + 1
            return z

        happy_Birthday(name, age)
        
        
        
        
    elif menu1 == 2:
        def addition(x,y):
            z = x+y
            return z
        def substraction(x,y):
            z = x-y
            return z
        def multiplication(x,y):
            z = x*y
            return z
        def division(x,y):
            z = x/y
            return z
    
        menu2=int(input(""" 
            Select menu:
            1. addition
            2. substraction
            3. multiplication
            4. division
            """))
        
        num_one = float(input("Input num1: "))
        num_two = float(input("Input num2: "))
        
        if menu2==1:
            addition(num_one, num_two)
        elif menu2==2:
            substraction(num_one, num_two)
        elif menu2==3:
            multiplication(num_one, num_two)
        elif menu2==4:
            division(num_one, num_two)
        else:
            print("Error")    
        
        print("Result is ")
    else:
        print("Error")
main() 


