"""
Make a program that is useful to determine if the integers X, Y and Z, provided by the user, are correct measures for the sides of a triangle and if they are, it must tell if it is an Equilateral, Isosceles or Scalene triangle.
Note: X, Y and Z are the sides of a triangle if they meet the following conditions:

    All numbers are greater than zero
    X + Y > Z
    X + Z > Y
    Y + Z > X

that is, the sum of two of the measures must be strictly greater than the third.

The equilateral triangle has 3 equal sides, the isosceles triangle has 2 equal sides, and the scalene triangle has 3 different sides.

Input

Three integers one in each row.

Output

Any of the following words: EQUILATERAL, ISOSCELES or SCALENE depending on the type of triangle for the given values.

Or, the phrase: IT IS NOT A TRIANGLE if the values ​​entered by the user do not correspond to the sides of a triangle, that is, they do not meet any of the conditions mentioned above.

Write only one of the 4 allowed messages using capital letters exactly as described.

Program execution example

>>>5

>>>5

>>>5

EQUILATERAL
"""

x = float(input("Input a value for side x: "))
y = float(input("Input a value for side y: "))
z = float(input("Input a value for side z: "))

if x >= 0 and y >= 0 and z >= 0:
    if x + y > z or x + z > y or y + z > x:
        if x == y == z:
            print("EQUILATERAL")
        elif x == y or y == z or x == z:
            print("ISOCELES")
        else:
            print("SCALENE")
    else:
        print("ERROR")
else:
    print("ERROR")