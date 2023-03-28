def count():#a
    chet = 0
    nechet = 0
    n = 0
    while n <= 10:
        if n % 2 == 0:
            chet += 1
        else:
            nechet += 1
        n += 1
    print(f'Кол-во четных чисел: {chet}')
    print(f'Кол-во нечетных чисел: {nechet}')

count()
print()

def count1(n = 0, chet = 0, nechet = 0):#b
    if n > 10:
        print(f'Кол-во четных чисел: {chet}')
        print(f'Кол-во нечетных чисел: {nechet}')
        return
    if n % 2 == 0:
        chet += 1
    else:
        nechet += 1
    count1(n + 1, chet, nechet)
count1()
