def purchase(fchair_type, famount_chairs):
    b_chairs_price = 700
    s_chairs_price = 900
    d_chairs_price = 1500
    if fchair_type == "B":
        func_total_chairs = b_chairs_price * famount_chairs
    elif fchair_type == "S":
        func_total_chairs = s_chairs_price * famount_chairs
    elif fchair_type == "D":
        func_total_chairs = d_chairs_price * famount_chairs
    else:
        print("Error on chair type")
    return(func_total_chairs)
def func_client_type(fclient_type, brute_price):
    if fclient_type == "R":
        if brute_price >= 10000 and brute_price < 20000: 
            net_chairs = brute_price - brute_price * 0.1 
        elif brute_price >= 20000: 
            net_chairs = brute_price - brute_price * 0.15 
        else:
            net_chairs = brute_price
        return net_chairs
    elif fclient_type == "F":
        net_chairs = brute_price - brute_price * 0.2
        return net_chairs
    else:
        print("Error")       
def main():
    chair_type = input("What chair type are you buying: B, S, D: ")
    amount_chairs = int(input("How many: "))
    brute_amount = purchase(chair_type, amount_chairs)
    client_type = input("What is the client type R or F: ")
    net_amount = func_client_type(client_type, brute_amount)
    print(f"Your undiscounted amount was {brute_amount} with your discount applied it is {net_amount}")
main()