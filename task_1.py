z=input("Введите знак операции: ")
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
def calculator(z1, a1, b1):
    if z=='+':
        return a+b
    elif z=='-':
        print(a-b)
    elif z=='*':
        print(a*b)
    elif z=='/':
        if (b!=0):
            print(a/b)
        else:
            print('На ноль делить нельзя!')

calculator(z,a,b)
