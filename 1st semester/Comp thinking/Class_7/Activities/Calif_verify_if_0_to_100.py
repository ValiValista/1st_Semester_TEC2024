def verify_cal(calif):
    if calif >= 0 and calif <=100:
        return True
    else:
        return False

def main():
    calif1 = int(input(""))
    calif2 = int(input(""))
    calif3 = int(input(""))

    if verify_cal(calif1) and verify_cal(calif2) and verify_cal(calif3):
        average = (calif1 + calif2 + calif3) / 3
        print(f"Average is {average}")
    else:
        print("Error 512")
    
main()