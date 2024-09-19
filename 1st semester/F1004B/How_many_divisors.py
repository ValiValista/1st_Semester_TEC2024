def mystery(n):
    result = 0
    for n in (1,  n):
        result += 1
    return result

def main():
    while True:
        x = int(input("Enter a number: "))
        print(mystery(x))

main()
