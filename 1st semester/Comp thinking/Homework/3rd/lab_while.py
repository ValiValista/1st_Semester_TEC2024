#A01647566

#Libs
import math
import random
import sys
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
        if num_tri_area and num2_tri_area >0:
            area_tri = (num_tri_area * num2_tri_area) / 2
            print(area_tri)
        else:
            error()
    def square_area():
        num_sqr_area = float(input("Enter a square's side: "))
        if num_sqr_area >0:
            area_sq = (num_sqr_area*num_sqr_area)
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

def menu_volumes():
    key_men_vols = int(input("""
Choose a shape to get its area 
1. Cone
2. Cube
3. Sphere
4. Exit

"""))
    def cone_volume():
        num_cone_volume = float(input("Enter a cone's height: "))
        num2_cone_volume = float(input("Enter a cone's radius: "))
        if num2_cone_volume and num2_cone_volume >0:
            volume_cone = (math.pi * num2_cone_volume**2) * (num_cone_volume/3)
            print(volume_cone)
        else:
            error()
    def cube_volume():
        num_cube_volume = float(input("Enter a cube's side: "))
        if num_cube_volume >0:
            volume_cube = num_cube_volume ** 3
            print(volume_cube)
        else:
            error()
    def sphere_volume():
        num_sphere_volume = float(input("Enter a sphere's radius: "))
        if num_sphere_volume > 0:
            volume_sphere = 4/3 * math.pi * num_sphere_volume**3
            print(volume_sphere)
        else:
            error()
    if key_men_vols == 1:
        cone_volume()
    elif key_men_vols == 2:
        cube_volume()
    elif key_men_vols == 3:
        sphere_volume()
    elif key_men_vols == 4:
        main()
    else:
        error()

def s_p_m():
    print("This program takes whole positive numbers and sums them up,\nwhen you put a negative number it ends and displays the sum, highest number, and average ")
    sumof = 0
    count = 0
    stored_m_number = 0
    while True:
        s_p_m_number = int(input("Enter a number: "))
        if s_p_m_number >0:
            sumof += s_p_m_number
            count += 1
            if s_p_m_number > stored_m_number:
                stored_m_number = s_p_m_number
        elif s_p_m_number <0:
            average = sumof / count
            print(f"The sum is {sumof}, the greatest number was {stored_m_number}, and the average is {average}")
            sleep(1)
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
3. Sum, Greater, Average
4. Menu Volumes
5. Fibonacci
6. 
7. Siracusa
8. 
9. Perfect number
10. Exit    
"""))
    while  True:
        if men_key == 1:
            sqrt_func()
        elif men_key == 2:
            menu_areas()
        elif men_key == 3:
            s_p_m()
        elif men_key == 4:
            menu_volumes()
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
            sys.exit(420)
        else:
            error()

main()