import math
import random

player_name = "Artur"

def roznica(num1, num2):
    result = num1 - num2
    return result

def pierwiastek(num1):
    if num1 >= 100:
        last_number = num1 % 100
    elif num1 < 100:
        last_number = num1 % 10
    num = num1
    if math.sqrt(num) == last_number:
        result = 1
    else:
        result = 0
    return result

def slownik():
    dictionary = {'pies': 'dog', 'kot': 'cat', 'chomik': 'hamster'}
    print("Oto słownik (wyrazy: pies, kot, chomik):")
    word = input("Wybierz słowo do wyświetlenia:")
    print(word.title(), "to po angielsku:", dictionary[word.lower()])

def walka(health, enemy):
    global player_name
    enemies = {"Zorg" : 100, "Demogorgon": 300, "Pająk" : 15, "Pełzacz": 50}

    enemy_health = enemies[enemy]

    while True:
        if enemy_health > 0:
            player_attack = random.randint(0,20)
            enemy_health -= player_attack
            print("Zadajesz", player_attack, "punktów obrażeń!")
            print(enemy, "ma już tylko", enemy_health, "punktów życia.")
            print("==========================")
        else:
            print("Wygrałeś!")
            winner = player_name
            break
        if health > 0:
            enemy_attack = random.randint(0,20)
            health -= enemy_attack
            print("Otrzymujesz", enemy_attack, "punktów obrażeń!")
            print("Pozostało Ci już tylko", health, "punktów życia,")
        else:
            print("Poległeś...")
            winner = enemy
            break
    return health, winner


print("Co robić")
print("[1] Różnica")
print("[2] Pierwiastek")
print("[3] Słownik")
print("[4] Walka")
wybierz = input("Wybierz:")
if wybierz == "1":
    num1 = input("Podaj pierwszą liczbę: ")
    num2 = input("Podaj drugą liczbę: ")
    print("Wynik: ", roznica(num1, num2))
elif wybierz == "2":
    num1 = int(input("Podaj liczbę:"))
    print("Ta liczba", end=" ")
    if pierwiastek(num1) == 0:
        print("nie", end=" ")
    print("kończy się swoim pierwiastkiem.")
elif wybierz == "3":
    slownik()
elif wybierz == "4":
    potwory = ("Zorg", "Demogorgon", "Pająk", "Pełzacz")
    enemy = random.choice(potwory)
    print("------------------------------------")
    print("Twoim przeciwnikiem będzie:", enemy)
    print("------------------------------------")
    walka(100, enemy)

