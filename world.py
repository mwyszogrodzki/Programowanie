#Wyjście na zewnątrz

fuel = 5
import Game

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

print(Game.twooprions("Tak", "Nie"))
