def fibonacci():
    s = [0, 1]
    num = 1
    while num < 100:
        num = s[-1] + s[-2]
        if num < 100:
            s.append(num)
    return s
print(fibonacci())
print()
def fibonacci2(n1 = 0, n2 = 1):
    if n2 >= 100:
        return []
    return [n2] + fibonacci2(n2, n1 + n2)
print(fibonacci2())