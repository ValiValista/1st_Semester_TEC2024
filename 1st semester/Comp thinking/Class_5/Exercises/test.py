def func1 (a, b):
     print(a, b)

def func2 (x, y):
     x = 10
     y *= 2
     func1 (y, x)

def main() :
     p = 2
     q = 3
     func2(p, q)
     func1(p, q)

main()