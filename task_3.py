print("Введите имя ")
name=input()
def hello():
    global name
    names=["Sasha","Alfina","Galiya","Azaliya"]
    if name in names:
        print(f"Привет,{name}")
    if name not in names:
        print(f"Привет, {name}. Рад знакомству!")
hello()