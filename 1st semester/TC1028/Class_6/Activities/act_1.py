def equivalent(funchour,funcmin,funcsec):
    totalsec=funchour*3600+funcmin*60+funcsec
    return totalsec

def main():
    print("Please enter your time:")
    hour=int(input("Hours: "))
    min=int(input("Minutes: "))
    sec=int(input("Seconds: "))
    totalsec=equivalent(hour,min,sec)
    print(f"Total seconds are {totalsec}.")
    
main()