import creator
import random
import potatoes
name, health, intelligence, knowledge, strenght = creator.charackter_creator()

food = random.randint(10, 20)
oxygen = random.randint(20, 40)
days = 1
inventory = []
fuel = 5
base = ["nic", "5 litrów paliwa", "nic", "racja żywnościowa", "nic", "2 racje żywnościowe",
                "nic", "nasiona ziemniaków", "nic", "ziemia", "nic", "10 litrów paliwa", "nic"]

def day_menu(food):
    print(food)
    food = food - 1

#Komunikat wstępny
print("To już miesiąc odkąd jesteś na planecie Kepler-452b. Twoja załoga zginęła podczas lądowania, ponieważ jeden z silników"
      " w Waszym statku uległ zniszczeniu. Na szczęście przed Wami na tej planecie było już wiele misji. Baza obok której wylądowaliście"
      "jest jedną z Wielu. Powodzenia w przetrwaniu.")

#Pętla codziennego menu
while food > 0 or oxygen > 0:
    print("[Dzień", days, "}")
    days += 1
    print("Pozostało Ci pożywienia na", food, "dni.")
    food -= 1
    print("Co chcesz zrobić?")
    print("[1] Przeszukać bazę")
    print("[2] Spróbować nawiązać kontakt z Ziemią")
    print("[3] Opuścić bazę")
    choice = input("Wybierz:")

    #Przeszukiwanie bazy
    if choice in ("1", "[1]"):
        thing = random.choice(base)
        if thing == "nic":
            print("Niestety po całodniowych poszukiwaniach nic nie znalazłeś. Idziesz spać")
            base.remove("nic")
            continue
        if thing == "5 litrów paliwa":
            print("Udało Ci się znaleźć 5 litrów paliwa!")
            fuel += 5
            base.remove("5 litrów paliwa")
            continue
        if thing == "10 litrów paliwa":
            print("Udało Ci się znaleźć 10 litrów paliwa!")
            base.remove("10 litrów paliwa")
            fuel += 10
            continue
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
                potatoes.growingpotatoes()
            else:
                print("Może uda się znaleźć ziemię?")
                ifsoil = random.choice(base)
                if ifsoil == "ziemia":
                    print("Bingo!")
                    potatoes.growingpotatoes()
                else:
                    print("Nie udało się, ale może jeszcze uda Ci się znaleźć...")
                    inventory.append(thing)
        if thing == "ziemia":
            print("Znalazłeś ziemię!")
            base.remove("ziemia")
            if "nasiona ziemniaków" in inventory:
                print("Masz już nasiona ziemniaków, teraz masz ziemię. Spróbujmy coś zasadzić!")
                potatoes.growingpotatoes()
            else:
                print("Może uda się znaleźć nasiona ziemniaków?")
                ifsoil = random.choice(base)
                if ifsoil == "nasiona ziemniaków":
                    print("Bingo!")
                    base.remove("nasiona ziemniaków")
                    potatoes.growingpotatoes()
                else:
                    print("Nie udało się, ale może jeszcze uda Ci się znaleźć...")
                    inventory.append(thing)
        if choice in ("2", "[2]")
            print("")

