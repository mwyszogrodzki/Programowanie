
number = int(input("Podaj liczbę:"))

def global_changes():
    global number
    number = number/2
    return

global_changes()
print(number)

