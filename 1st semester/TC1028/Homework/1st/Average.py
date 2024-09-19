"""
Made by Viri V. #A01647566
Problem: Take 3 values and average them
Inputs:
    time1
    time2
    time3
Outputs:
    average
"""
print('\nThis program takes your 3 running times for the week then averages them\n')
# inputting
time1 = int(input("What was your run time in minutes this monday? "))
time2 = int(input("What was your run time in minutes this wednesday? "))
time3 = int(input("What was your run time in minutes this friday? "))

# Processing
# Takes the 3 inputs and divides them by 3 to get an average
average = ((time1 + time2 + time3)/3)

# Outputting
print(f"\nYour average time this week was that of {average:.3f} minutes\n")