from random import randint
import copy

def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def list_print(f_list):
    for i in range(len(f_list)):
        print(f_list[i], end = " ")
    print()

def main():
    list1 = []
    for i in range(5):
        list1.append(randint(1, 100))

    print(f"List is {list1}\n")
    print(f"List max is {max(list1)} and list min is {min(list1)}\n")

    list_ord = []
    list_ord = list1.copy()
    list_ord.sort(reverse=True)
    print(f"The ordered is {list_ord}\n")

    sum_even=0
    sum_odd=0
    for i in range(len(list_ord)):
        if check_even(list_ord[i]):
            sum_even+=list_ord[i]
        else:
            sum_odd+=list_ord[i]
    print(f"The sum of the even numbers is {sum_even}\n")
    print(f"The sum of the odd numbers is {sum_odd}\n")

    sum_even_indexes=0
    for i in range(0,len(list_ord),2):
        sum_even_indexes+=list_ord[i]
    print(f"The sum of the numbers in even indexes is {sum_even_indexes}\n")





main()
