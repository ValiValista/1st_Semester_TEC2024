#Libs
import math
import random
from time import sleep

def error():
    print("Error, exception handled")
    sleep(2)
    main()

def sqrt_func():
    sqrt_num = float(input("Enter a number: "))
    if sqrt_num >0:
        sqrt_solve = math.sqrt(sqrt_num)
        print(sqrt_solve)

    else:
        error()
    sleep(1)
    main()

def menu_areas():
    key_men_areas = int(input("""
Choose a shape to get its area 
1. Triangle
2. Square
3. Circle
4. Exit

"""))
    def triangle_area():
        num_tri_area = float(input("Enter a triangle's height: "))
        num2_tri_area = float(input("Enter a triangle's width: "))
        if num_tri_area >0:
            area_tri = (num_tri_area * num2_tri_area) / 2
            print(area_tri)
        else:
            error()
    def square_area():
        num_sqr_area = float(input("Enter a square's height: "))
        num2_sqr_area = float(input("Enter a square's width: "))
        if num_sqr_area >0:
            area_sq = (num_sqr_area * num2_sqr_area)
            print(area_sq)
        else:
            error()
    def circle_area():
        num_circle_area = float(input("Enter a circle radius: "))
        if num_circle_area > 0:
            area_circle = num_circle_area**2 * math.pi
            print(area_circle)
        else:
            error()
    if key_men_areas == 1:
        triangle_area()
    elif key_men_areas == 2:
        square_area()
    elif key_men_areas == 3:
        circle_area()
    elif key_men_areas == 4:
        main()
    else:
        error()

def fibonacci():
    print("Fibonacci up to n")
    a, b, n = 0, 1, int(input("Enter a number: "))

    while b <= n:
        print(b)
        a, b = b, a + b
    main()
    sleep(1)

def siracusa():
    sira = int(input("input: "))
    print(sira)
    while sira != 1:
        if sira >0:
            if sira % 2 == 0:
               sira = sira // 2
               print(sira)
            else:
                sira = (sira * 3) + 1
                print(sira)
        else:
            error()
    sleep(1)
    main()

def perfect():
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
        error()
    sleep(1)
    main()

def main():
    men_key = int(input(""" 
Please select the program you wish to use
1. Square root
2. Menu Areas
5. Fibonacci
7. Siracusa
9. Perfect number
10. Exit    
"""))
    while True:
        if men_key == 1:
            sqrt_func()
        elif men_key == 2:
            menu_areas()
        elif men_key == 3:
            error()
        elif men_key == 4:
            error()
        elif men_key == 5:
            fibonacci()
        elif men_key == 6:
            error()
        elif men_key == 7:
            siracusa()
        elif men_key == 8:
            error()
        elif men_key == 9:
            perfect()
        elif men_key == 10:
            break
        else:
            error()

main()