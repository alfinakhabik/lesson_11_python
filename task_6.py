n = int(input('Введите число: '))
def factorial(n):#a
    i = 1
    while n > 1:
        i *= n
        n -= 1
    print(i)

factorial(n)
print()
def factorial1(n):#b
    if n == 0:
        return 1
    return factorial1(n - 1) * n
print(factorial1(n))

