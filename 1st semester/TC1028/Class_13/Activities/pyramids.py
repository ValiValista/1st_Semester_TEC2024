# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()
#
# for i in range(5):
#      print((("*" * 5 + " ") + "\n" ))



"""
Pyramids
"""


n=int(input("Enter the number of rows: "))
for i in range (1, n+1):
    print("*"*i) #print the stars in increasing order

n=int(input("Enter the number of rows: "))
for i in range (1, n+1):
    print(" "*i,end=" ")
    for j in range (i, n+1):
        print("*",end="")
    print()