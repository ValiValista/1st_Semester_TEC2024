def check_a_lessthan_b(func_a,func_b):
    if func_a < func_b:
        return True
    else:
        return False
def main():
    a = int(input("Input number: "))
    b = int(input("Input number: "))
    while check_a_lessthan_b(a,b):
        a += 1
        if a % 2 == 0:
            print(a)
        else:
            pass
main()