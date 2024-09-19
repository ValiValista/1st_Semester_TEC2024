"""
Inputs: 
    lenght
    width 
    choice of a or p

"""

def area_rect(func_input_lenght,  func_input_width):
        area_rect = func_input_lenght * func_input_width
        return area_rect

def perimeter_rect(func_input_lenght, func_input_width):
        func_perimeter_rect = func_input_lenght + func_input_width
        return func_perimeter_rect

def main():

    
    print("""
Choose what part of the rectangle do you wnat to get
1. Area
2. Perimeter
3. Both

""")
    main_menu = int(input(""))
    
    width = float(input("""
Input width: """))
    lenght = float(input("""
Input lenght: """))
    
    print_pr = perimeter_rect(width, lenght)
    print_ar = area_rect(width, lenght)
    
    if main_menu == 1:
        
        print(f"The area is {print_ar}\n")
        
    elif main_menu == 2:
        
        print(f"The perimeter is {print_pr}\n")   
        
    else:
        print(f"Perimeter is {print_pr} and area is {print_ar}\n")
             


    
    
    
    
main()