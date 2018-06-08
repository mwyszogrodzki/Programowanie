import random

def nietak():
    print("Coś poszło nie tak, spróbuj jeszcze razm")

def character_creator():
    print("Witaj w kreatorze postaci! Jak chcesz się nazywać?")
    character_name = input(">")
    while True:
        print("Podaj wiek w zakresie od 18 do do 150")
        character_age = int(input(">"))
        if character_age < 18 or character_age > 150:
            nietak()
        else:
            break
    while True:
        print("Kobieta czy mężczyzna?")
        gender_input = input(">")
        if gender_input.lower() in ("k", "kobieta", "kobietą"):
            character_gender = "k"
            break
        elif gender_input.lower() in ("m", "mężczyzna", "mezczyzna"):
            character_gender = "m"
            break
        else:
            nietak()
    while True:
        print("Jaką rasę wybierasz?")
        print("[1] Ork")
        print("[2] Mag")
        print("[3] Krasnolud")
        print("(podaj numer)")
        character_race = int(input(">"))
        if character_race in (1, 2, 3):
            break
        else:
            nietak()
            continue

    points = random.randint(40, 90)
    character = {"Zwinność": 0, "Budowa": 0, "Siła": 0, "Szybkość": 0, "Inteligencja": 0}

    print("Masz do dyspozycji", points, "punktów.")
    print("Jak chcesz podzielić swoje punkty? Żadna z cech nie może mieć wartości mniejszej niż 5 i większej od 20")

    for i in character:
        while points > 0:
            print()
            print("Pozostało Ci", points, "punktów.")
            choice = int(input("Ile punktów dla " + i + " ?:"))
            if choice >= 5 and choice <= 20:
                if choice > points:
                    choice = points
                character[i] = choice
                points -= choice
            else:
                print("Wartość powinna być większa lub równa 5 i mniejsza bądź równa 20")
                continue
            break
