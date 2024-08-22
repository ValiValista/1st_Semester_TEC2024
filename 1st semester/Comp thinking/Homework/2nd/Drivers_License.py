"""
Driver license

A person can obtain its driver's license if they are of legal age and have official identification.

Write a Python program that reads a person's age and if they have (y/n) official identification.

Output must show Yes if you can obtain your license or No if you cannot obtain it

Input

person's age

The letter y or n indicates whether or not you have official identification. The letter is lowercase.

Output

The word Yes or No depending on whether or not the person can get their driver's license. Note that the word goes with the first letter capitalized.

Program execution example:

>>>21

>>>y

Yes

"""

print("To get a driver's license you need to be over 18 and have an official identification")
print("This program ask you for your age and if you have an official identification\n")
age = int(input("Please input a whole number 0-99+ for your age: "))
has_id = input("Please input \"y\" or \"n\" ")

if age > 18:
    if has_id == "y":
        print("Yes")
    else:
        print("You cannot get a driver's license, you are missing an official identification")
else:
    print("You cannot get a driver's license, get older")
