# Importowanie zewnętrznych funkcji
import creator
import random
import potatoes
name, health, intelligence, knowledge, strenght = creator.charackter_creator()


#Wstępne ustalenia
food = random.randint(10, 20)
oxygen = random.randint(20, 40)
days = 1
inventory = []
fuel = 5
ifgarden = 0
base = ["nic", "5 litrów paliwa", "nic", "racja żywnościowa", "nic", "2 racje żywnościowe",
                "nic", "nasiona ziemniaków", "nic", "ziemia", "nic", "10 litrów paliwa", "nic"]

#Funkcje
def misson():
    axis_x = 0
    axis_y = 0
    choice = ""
    mission_inventory = []


    while choice != "powrót":
        print("Wyszedłeś z bazy, przed Tobą bezkresna planeta. Co robisz?")
        print("[1} Idę pieszo")
        print("[2] Jadę łazikiem")
        print("(Paliwa starczy na:", fuel*10, "kilometrów)")
        choice = input("Wybieram: ")
        break

def charackter_creator():
    """Stwórz nową postać"""
    health = 75
    print("KREATOR POSTACI")
    name = input("Podaj imię swojej postaci:")
    gender = input("Kobieta [K] czy mężczyzna [M]?")
    if gender.lower() in ("k", "[k]", "kobieta"):
        gender = 0
    elif gender.lower() in ("m", "[m]", "mężczyzna", "mezczyzna"):
        gender = 1
    print("Jaką rolę chcesz przybrać?")
    print("[1] Technik   [2] Biolog")
    print("[3] Żołnierz")
    role = input("Wybierz rolę:")
    if role.lower() in ("1", "technik"):
        intelligence = random.randrange(50, 100)
        knowledge = random.randrange(25, 75)
        strenght = random.randrange(25, 75)
    elif role.lower() in ("2", "[2]", "biolog"):
        intelligence = random.randrange(50, 100)
        knowledge = random.randrange(50, 100)
        strenght = random.randrange(1, 50)
    elif role.lower() in ("3", "[3]", "żołnierz", "zolnierz"):
        intelligence = random.randrange(15, 50)
        knowledge = random.randrange(15, 50)
        strenght = random.randrange(50, 100)
        health += 15

    return name, health, intelligence, knowledge, strenght

def searching(food, fuel, ifgarden):
    thing = random.choice(base)
    if thing == "nic":
        print("Niestety po całodniowych poszukiwaniach nic nie znalazłeś. Idziesz spać")
        base.remove("nic")
    if thing == "5 litrów paliwa":
        print("Udało Ci się znaleźć 5 litrów paliwa!")
        fuel += 5
        base.remove("5 litrów paliwa")
    if thing == "10 litrów paliwa":
        print("Udało Ci się znaleźć 10 litrów paliwa!")
        base.remove("10 litrów paliwa")
        fuel += 10
    if thing == "racja żywnościowa":
        print("Udało Ci się znaleźć rację żywnościową na 5 dni!")
        base.remove("racja żywnościowa")
        food += 5
    if thing == "2 racje żywnościowe":
        print("Udało Ci się znaleźć racje żywnościowe na 10 dni!")
        base.remove("2 racje żywnościowe")
        food += 10
    if thing == "nasiona ziemniaków":
        print("Znalazłeś nasiona ziemniaków!")
        base.remove("nasiona ziemniaków")
        if "ziemia" in inventory:
            print("Masz już ziemię, teraz masz nasiona ziemniaków. Spróbumy coś zasadzić!")
            ifgarden += 1
        else:
            print("Może uda się znaleźć ziemię?")
            ifsoil = random.choice(base)
            if ifsoil == "ziemia":
                print("Bingo!")
                ifgarden += 1
            else:
                print("Nie udało się, ale może jeszcze uda Ci się znaleźć...")
                inventory.append(thing)
    if thing == "ziemia":
        print("Znalazłeś ziemię!")
        base.remove("ziemia")
        if "nasiona ziemniaków" in inventory:
            print("Masz już nasiona ziemniaków, teraz masz ziemię. Spróbujmy coś zasadzić!")
            ifgarden += 1
        else:
            print("Może uda się znaleźć nasiona ziemniaków?")
            ifsoil = random.choice(base)
            if ifsoil == "nasiona ziemniaków":
                print("Bingo!")
                base.remove("nasiona ziemniaków")
                ifgarden += 1

            else:
                print("Nie udało się, ale może jeszcze uda Ci się znaleźć...")
                inventory.append(thing)
    return food, fuel, ifgarden

def show_inventory():
    if inventory == 0:
        print("Twój ekwipunek jest pusty")
    else:
        for i in inventory:
            print(i, end=" | ")
        print("\n")

# Komunikat wstępny
print("To już miesiąc odkąd jesteś na planecie Kepler-452b. \n Twoja załoga zginęła podczas lądowania, ponieważ jeden z silników \n"
      " w Waszym statku uległ zniszczeniu. Na szczęście przed Wami na tej planecie było już wiele misji. \n Baza obok której wylądowaliście "
      "jest jedną z Wielu. Powodzenia w przetrwaniu. \n")

# Pętla codziennego menu
while food > 0 or oxygen > 0:
    print("[Dzień", days, "}")
    if ifgarden:
        if days % 15 == 0:
            food += 10
            print("Zbiory ziemniaków!")
    print("Pozostało Ci pożywienia na", food, "dni.")
    print("Co chcesz zrobić?")
    print("[1] Przeszukać bazę")
    print("[2] Spróbować nawiązać kontakt z Ziemią")
    print("[3] Opuścić bazę")
    print("[4} Wyświetlić ekwipunek")
    choice = input("Wybierz:")

    # Przeszukiwanie bazy
    if choice in ("1", "[1]"):
        if base:
            food, fuel, ifgarden = searching(food, fuel, ifgarden)
        else:
            print("Już przeszukałeś całą bazę. Czas na coś innego!")
            continue
    #Połączenie z ziemią
    if choice in ("2", "[2]"):
            print("Tutaj będzie próba połączenia")
    #Wyjście poza bazę
    if choice in ("3", "[3]"):
        print("Tutaj będzie wyjście na zewnątrz")
    #Wyświelenie ekwipunku
    if choice in ("4", "[4]"):
        show_inventory()
        continue
    #Działania na koniec dnia
    days += 1
    food -= 1

