import random
import time
import pickle

actions = { 1 : "Rozmawiam z bezdomnym na rynku",
            2 : "Idę do baru",
            3 : "Wracam do domu",
            4 : "Idę do ratusza",
            5 : "Idę na rynek",
            6 : "Idę do sklepu",
            7 : "Zaglądam do ekwipunku",
            8 : "Wychodzę z lotniska",
            9 : "Idę do siedziby partii",
            10 : "Idę do hotelu",
            11 : "Idę na dworzec",
            99 : "Zapisz grę"}

things = { '1' : {"name": "Miecz Prezydencki",
                "type": 1,
                "value": 50,
                "cost": 5000},
'2' : {"name": "Tabletka uzdrawiająca",
                "type": 2,
                "value": 10,
                "cost": 200},
'3': {"name": "Czerwony talizman",
                "type": 3,
                "value": 20,
                "cost": 15},
'4': {"name": "Szabelka marszałkowska",
      "type": 1,
      "value": 20,
      "cost": 2000},
'5': {"name": "Szpon Eosapiensa",
      "type": 3,
      "value": 0,
      "cost": 1000}}

class character(object):
    money = 500
    def __init__(self, name):
        #Ustalenia wstępne
        self.name = name
        self.health = 100
        self.level = 1
        self.exp = 0
        self.ifTalkedWithGrazynka = 0
        self.ifTalkedWithHomeless = 0
        self.ifGetMessage = 0
        self.eosapiens_howMany = 3
        self.money = 500
        self.inventory = []
        self.possibleActions = [1, 2, 3, 4, 6, 7, 99]

        #Przywitanie gracza po stworzeniu postaci, losowanie parametrów
        print("Witaj na planecie Darwin4", self.name, ", cieszymy się, że przeniosłeś się do Nowej Polski.")
        print("Sprawdźmy jak wygląda Twój profil w systemie PolakID:")
        self.strength = random.randint(50,100)
        self.intelligence = random.randint(50,100)
        self.agility = random.randint(50,100)
        print("Siła:", self.strength, "/ 100")
        time.sleep(2)
        print("Inteligencja:", self.intelligence, "/ 100")
        time.sleep(2)
        print("Zwinność:", self.agility, "/ 100")
        time.sleep(2)
        print("Stan konta:", self.__class__.money, "złotych")
        print("Dziękujemy, możesz już wrócić do miasta")
        time.sleep(2)

    def healthPlus(self, value):
        #Dodawanie punktów życia
        self.health += value
        print("*** PRZYBYŁO CI", value, "PUNKTÓW ŻYCIA***")

    def healthMinus(self, value):
        # Odejmowanie punktów życia
        self.health -= value
        print("*** UTRACIŁEŚ", value, "PUNKTÓW ŻYCIA***")

    def moneyMinus(self, value):
        #Zmniejsza stan konta
        self.__class__.money -= value
        print("[STAN KONTA:", self.__class__.money, "ZŁ]")

    def moneyAdd(self, value):
        #Zwiększa stan konta
        self.__class__.money += value
        print("[STAN KONTA:", self.__class__.money, "ZŁ]")

    def inventoryAdd(self, item):
        self.inventory.append(item)
        print("""=== Do DWOJEGO EKWIPUNKU DODANO:""", things[item]["name"], "===")

    def inventoryRemove(self, item):
        self.inventory.remove(item)
        print("""=== Do DWOJEGO EKWIPUNKU DODANO:""", things[item]["name"],"===")

    def checkInventory(self, name):
        if name in self.inventory:
            result = 1
        else:
            result = 0
        return result

    def inventoryShow(self):
        number = 1
        print("[TWÓJ EKWIPUNEK]")
        for i in self.inventory:
            print("[", number ,"]", things[i]['name'])
            number += 1
        print("[0] Wróć")
        input(">>")
    def attack(self, enemy):

        self.attackValue = self.strength*0.2 + self.agility*.1 + random.randint(1,10)
        self.attackValue -= self.attackValue % 1
        print("## Atakujesz z siłą", self.attackValue,"##")
        enemy.defence(self.attackValue)

    def defence(self, attackValue):
        self.defenceValue = attackValue - random.randint(1,5)
        self.health -= self.defenceValue
        print("## Pozostało Ci", self.health, "punktów życia. ##")
    def expAdd(self, value):
        self.exp += value
        print("+++ ZYSKAŁEŚ", value, "PUNKTÓW DOŚWIADCZENIA +++")
        print("+++   ", 100 - self.exp, "DO NASTĘPNEGO POZIOMU    +++")
        if self.exp >= 100:
            levelUp(self.level+1)

class mob(object):

    def __init__(self, MobName, health, attackLevel):
        self.MobName = MobName
        self.health = health
        self.attackLevel = attackLevel

    def attack(self):
        self.attackValue = self.attackLevel * random.randint(1,10)
        print("##", self.MobName.title(), "atakuje z siłą", self.attackValue,"##")
        player.defence(self.attackValue)

    def defence(self, attackValue):
        self.defenceValue = attackValue - random.randint(1,5)
        self.health -= self.defenceValue
        print("##", self.MobName.title(), "pozostało", self.health, "punktów życia. ##")

def possibleAction(value):
    global actions
    options = []
    for i in value:
        options.append(i)
    print("Co robisz?")
    number = 1
    for i in options:
        print("[", number ,"]", actions[i])
        number += 1
    choice = input(">>")
    return choice
def levelUp(level):
    if level == 2:
        player.possibleActions.append('11')
        print("BRAWO!")
        print("Awansowałeś! Masz już 2 poziom!")



def endgame():
    print("Niestety poległeś... Planeta Darwin4 nie jest jednak tak przyjazna jak się wydawało.")
    menu()

def battle(enemy):
    winner = 0

    while True:
            if player.health >= 0:
                player.attack(enemy)
            elif player.health < 0:
                print("Przegrałeś.")
                endgame()
                break
            if enemy.health >= 0:
                enemy.attack()
            elif enemy.health < 0:
                print("Wygrałeś!")
                winner += 1
                break
            if player.health < 0:
                print("Przegrałeś.")
                endgame()
            elif player.health <= 10:
                while True:
                    print("Pozostało Ci mniej niż 10 punktów życia. Czy chcesz się wycofać?")
                    print("[1] Tak, uciekam")
                    print("[2] Nie, walczę dalej")
                    print("[3] Weź tabletkę uzdrawiającą")
                    choice = input(">>")
                    if choice == "1":
                        print("Uciekłeś")
                        break
                    elif choice == "2":
                        break
                    else:
                        if player.checkInventory("Tabletka uzdrawiająca"):
                            player.inventoryRemove("Tabletka uzdrawiająca")
                            player.healthPlus(10)
                            break
                        else:
                            print("Niestety nie masz ich w swoim ekwipunktu.")
                            continue
    input(">>")
    return winner

def look_in_inventory():
    inventory = player.inventory
    print("Oto Twój ekwipunek:")
    player.inventoryShow()

def lotto():
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    number3 = random.randint(0, 9)
    number4 = random.randint(0, 9)
    number5 = random.randint(0, 9)
    number6 = random.randint(0, 9)

    user1 = input(">> Podaj pierwszą liczbę: ")
    user2 = input(">> Podaj drugą liczbę: ")
    user3 = input(">> Podaj trzecią liczbę: ")

    correct = 0

    if int(user1) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user1 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user1 + " nie szostała wylosowana")

    if int(user2) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user2 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user2 + " nie szostała wylosowana")

    if int(user2) in [number1, number2, number3, number4, number5, number6]:
        print("Liczba " + user3 + " została wylosowana.")
        correct += 1
    else:
        print("Liczba " + user3 + " nie szostała wylosowana")

    print("Trafiłeś na " + str(correct) + " spośród 6 liczb")
    print("Szczęśliwe liczby to: ", number1, number2, number3, number4, number5, number6)
    return correct

def zgadywanie():
    number = random.randint(1, 100)
    user_number = ' '
    times = 6
    fails = 0
    succes = 0
    while user_number != number:
        if times > 0:
            user_number = input("Wybierz liczbę od 1 do 100: ")
            if int(user_number) > number:
                print("Wylosowana liczba jest mniejsza")
                times -= 1
                fails += 1
                print("Zostało Ci", times, "prób.\n")
            elif int(user_number) == number:
                print("\n======================")
                print("Bingo!")
                fails += 1
                print("Miałeś", fails, "prób")
                succes = 1
                break
            else:
                print("Wylosowana liczba jest większa")
                times -= 1
                fails += 1
                print("Zostało Ci", times, "prób.\n")
        else:
            print("Game Over!")
            break
    return succes

def shop():
    #Funkcja wyświetla sklep
    print("||| SKLEP |||")
    time.sleep(1)
    print("Witaj w sklepie, sprawdźmy najpierw Twój stan konta:")
    print("[ Masz", player.money, "złotych. ]")
    time.sleep(2)
    while True:
        print("Chcesz?")
        print("[1] Kupić przedmioty")
        print("[2] Sprzedać przedmioty")
        print("[3] Wrócić do miasta")
        choice = input(">>")
        if choice == '1':
            print("Dzisiaj w naszej ofercie:")
            if player.level == 1:
                # Możliwe zakupy na pierwszym poziomie
                possibleItems = ('1', '2')
                print("[0] Wróć")
                for i in possibleItems:
                    print("[", i, "]", things[i]["name"], "| Cena:", things[i]["cost"])
                choice = input(">>")
                if choice == 0:
                    continue
                print(things[choice]['cost'])
                print(player.money)
                if things[choice]['cost'] <= player.money:
                    player.inventoryAdd(choice)
                    player.moneyMinus(things[choice]['cost'])
                else:
                    print("Masz za mało pieniędzy na ten przedmiot.")
                    continue
            elif player.level == 2:
                # Możliwe zakupy na drugim poziomie
                possibleItems = ('1', '2')
                number = 1
                for i in possibleItems:
                    print("[", i, "]", things[i]["name"], "| Cena:", things[i]["cost"])
                choice = input(">>")
                if things[choice]['cost'] >= player.money:
                    player.inventoryAdd(choice)
                    player.moneyMinus(things[choice]['cost'])
                else:
                    print("Masz za mało pieniędzy na ten przedmiot.")
                    continue
            elif player.level == 3:
                # Możliwe zakupy na trzecim poziomie
                possibleItems = ('1', '2')
                number = 1
                for i in possibleItems:
                    print("[", i, "]", things[i]["name"], "| Cena:", things[i]["cost"])
                choice = input(">>")
                if things[choice]['cost'] >= player.money:
                    player.inventoryAdd(choice)
                    player.moneyMinus(things[choice]['cost'])
                else:
                    print("Masz za mało pieniędzy na ten przedmiot.")
                    continue
            continue

        elif choice == '2':
            print("Który przedmiot?")
            print("[0] Wróć")
            for i in player.inventory:
                print("[", i, "]", things[i]["name"], "| Cena:", things[i]["cost"]*0.8)
            choice = input(">>")
            if choice == 0:
                continue
            player.inventoryRemove(choice)
            player.moneyAdd(things[choice]["cost"]*0.8)
            continue
        else:
            break

def decoding():
    coded = "Ipnkdc oydzredntg. Iygiów w podyzd. Oyzraptlj oyzdmpwę."
    decoded = "Koniec prezydenta. Kraków w operze. Przygotuj przemowę."
    number = 0
    for i in coded:
        while True:
            if i == " " or i == ".":
                number += 1
                break
            else:
                print("GA-DE-RY-PO-LU-KI")
                print("Literka:", i)
                letter = input(">>")
                if letter.lower() == decoded[number].lower():
                    print("Dobrze.")
                    number += 1
                    break
                else:
                    continue
    print("Rozszyfrowana wiadomość to:")
    print('"', decoded, '"')

def radom():
    #Poziom drugi gry
    print("Witaj w Radomiu!")

def krakow():
    print("Witaj w Krakowie!")
    #Poziom trzeci gry

def warszawa():
    global player
    print("||| RYNEK |||")
    time.sleep(2)
    print("Znajdujesz się na rynku miejscowości Nowa Warszawa na planecie Darwin4.")
    time.sleep(2)
    print("To już ponad 300 lat, odkąd Polska przeniosła się na tę planetę.")
    time.sleep(2)
    print("Dzień wydaje się spokojny, powoli spacerujesz poszukując zajęcia.")
    time.sleep(2)
    print("Na ławce widzisz miejscowego bezdomnego, ciężko sobie wyobrazić ten rynek bez niego.")
    time.sleep(2)
    while True:
        if player.ifTalkedWithHomeless:
            actions[1] = "Idziesz na rynek"

        choice = possibleAction(player.possibleActions)
        # Gracz idzie na rynek
        if choice == "1":
            #Jeśli gracz nie rozmawiał z bezdomnym to nie pojawią się potwory
            if player.ifTalkedWithHomeless == 0:
                print("[BEZDOMNY] Kierownik nie boi się tak samemu tu spacerować?")
                print("[1] Niby dlaczego?")
                print("[2] W tym mieście niczego się nie boję!")
                choice = input(">>")
                if choice == "1":
                    print("Bo brakuje mi jednej złotówki...")
                    print("[1] No dobrze")
                    print("[2] Nie mam mowy")
                    choice = input(">>")
                    if choice == "1":
                        print("Kierowniku kochany!")
                        player.moneyMinus(1)
                    else:
                        print("Co się dzieje z tym światem, jednej złotóweczki nawet nie dadzą...")
                    print("[1] Powiesz mi w końcu co się dzieje?")
                    print("[2] Odchodzisz")
                    choice = input(">>")
                    if choice == "1":
                        print("W ostatnim czasie zapuszczają się aż tutaj eosapiensy. Słyszałem, że w ratuszu można zdobyć nagrodę za zabicie kilku.")
                        print("[1] Dziękuję!")
                        print("[2] Masz tu jeszcze jedną złotówkę")
                        player.ifTalkedWithHomeless += 1
                        choice = input(">>")
                        if choice == "1":
                            print("Odchodzisz")
                        else:
                            player.moneyMinus(1)
                            print(
                                "Dziękuję! Kierownik zobaczy, mam tutaj coś w zamian, na skupie nic mi za to nie chcieli dać, ale może się przyda...")
                            player.inventoryAdd("3")
                    else:
                        print("Odszedłeś.")
                elif choice == "2":
                    print("Jeszcze zobaczysz jak bardzo się mylisz...")
                continue
            #Za to pojawią się jeśli rozmawiał
            else:
                #Program losuje czy pojawi się eosapiens
                random_binary = random.randint(0,3)
                if random_binary == 1:
                    if player.eosapiens_howMany > 0:
                        print("||| RYNEK |||")
                        print("Z oddali widzisz zbliżającego się Eosapiensa. Co robisz?")
                        print("[1] Walczę!")
                        print("[2] Uciekam!")
                        choice = input(">>")
                        if choice == "1":
                            eosapiens1 = mob("Eosapiens", 50, 1)
                            if battle(eosapiens1):
                                player.inventoryAdd("5")
                                player.expAdd(10)
                                player.eosapiens_howMany -= 1
                                continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        print("||| RYNEK |||")
                        print("Ku Twojemu zaskoczeniu na rynku panuje cisza i spokój.")
                        input(">>")
                else:
                    print("||| RYNEK |||")
                    print("Ku Twojemu zaskoczeniu na rynku panuje cisza i spokój.")
                    input(">>")

        # Gracz idzie do ratusza
        elif choice == '4':
            if player.ifTalkedWithGrazynka == 0:
                print("||| RATUSZ |||")
                time.sleep(1)
                print("Wchodzisz do urzędu, w środku jest prawie pusto. Jedna kobieta rozmawia z robotem w okienku.")
                time.sleep(1)
                print("Na wielkich ekranach faktycznie wyświetla się ogłoszenie o nagrodzie.")
                time.sleep(1)
                print("Znajdujesz jedynego człowieka z urzędu z którym możesz porozmawiać.")
                time.sleep(1)
                print(
                    "Kobieta z krótkimi włosami w średnim wieku, siedzi za okienkiem popijając kawę i rozwiązując krzyżówki na swoim tablecie.")
                time.sleep(1)
                print("> Przepraszam!")
                time.sleep(2)
                print("Odpowiedział Ci cisza, Pani Grażynka nadal jest zajęta swoją przerwą.")
                print("[1] Wołasz jeszcze raz, tym razem głośniej.")
                print("[2] Czekasz")
                choice = input(">>")
                if choice == "1":
                    print("Czego?! Nie widzi, że mam przerwę? Poczekaj chwilę.")
                print("Czekasz.")
                time.sleep(2)
                print("Czekasz.")
                time.sleep(1)
                print("Kobieta w końcu kończy kawę i podchodzi do Ciebie.")
                print("[KOBIETA] O co chodzi?")
                print("[1] Widziałem, że jest ustalona nagroda za zabicie eosapiensów. Mogę dostać więcej szczegółów?")
                #choice = input(">>")
                print(
                    "Kochaniutki, to proste, zabij 3 z nich i prznieś mi po jednym szponie od każdego. Nagroda to 5 tysięcy")
                print("[1] Dziękuję!")
                print("[2] Tylko tyle...?")
                choice = input(">>")
                if choice == "1":
                    print("Odchodzisz.")
                else:
                    print("Czego by jeszcze chciał? Żebym ja tam poszła i za niego zabijała?")
                    time.sleep(1)
                    print("Pani Grażynka odwraca się niezadowolona i odchodzi.")
                player.ifTalkedWithGrazynka += 1
            elif player.ifTalkedWithGrazynka >= 900:
                print("Kochaniutki, już raz dostałeś nagrodę, nic więcej dla Ciebie nie mamy.")
            else:
                print("Witaj kochaniutki, zabiłeś już te potwory?")
                print("[1] Nie, jeszcze nie")
                print("[2] Tak, proszę spojrzeć!")
                choice = input(">>")
                if choice == "1":
                    print("No to na co czekasz, leć ich szukać!")
                else:
                    EosapiensClawCount = 0
                    for i in player.inventory:
                        if i == "5":
                            EosapiensClawCount += 1
                    if EosapiensClawCount >= 3:
                        print("Faktycznie, gratuluję.")
                        time.sleep(1)
                        print("Oto Twoje zasłużone 5 tysięcy złotych.")
                        player.moneyAdd(5000)
                        player.ifTalkedWithGrazynka = 900
                print("Odchodzisz.")

        # Gracz idzie do baru
        elif choice == '2':
            #Jeśli gracz nie dostanie wiadomości
            if player.ifGetMessage == 0:
                print("||| BAR |||")
                time.sleep(1)
                print("Wchodzisz do swojego ulubionego baru. Jest trochę obskurny, ale mają najlepsze ceny.")
                time.sleep(1)
                print("Dzisiaj jednak jest wyjątkowo dużo ludzi. Zagadujesz mężczyznę po Twojej prawej stronie.")
                print("[1] Co tu się dzieje?")
                print("[2] Coś się dzieje ostatnio w mieście?")
                choice = input(">>")
                if choice == "1":
                    print("Nie widzisz? Są zawody w siłowaniu się na rękę!")
                    print("Może weźmiesz udział?")
                    print("[1] Jasne!")
                    print("[2] Wolałbym nie...")
                    choice = input(">>")
                    if choice == "1":
                        print("Chcesz się założyć, że wygrasz? Wpłać 10zł, a jeśli wygrasz - dostaniesz 100zł!")
                        print("[1] Dobrze, masz tu 10zł")
                        print("[2] Nie")
                        choice = input(">>")
                        if choice == "1":
                            player.moneyMinus(10)
                            print(
                                "Podchodzisz do stołu. Twój przeciwnik wydaje się być zdecydowanie od Ciebie większy...")
                            if player.strength > 80 or player.agility > 85:
                                print("Walka trwa!")
                                time.sleep(1)
                                print("Idzie Ci bardzo dobrze, ręka przeciwnika przechyla się w jego kierunku.")
                                time.sleep(1)
                                print("Jesteś coraz bliżej wygranej!")
                                time.sleep(1)
                                print("Pokonany!")
                                time.sleep(1)
                                print("Wszyscy w barze Ci gratulują")
                                time.sleep(1)
                                player.expAdd(10)
                                time.sleep(1)
                                player.moneyAdd(100)
                            elif player.strength > 70 or player.agility > 75:
                                print("Walka trwa!")
                                time.sleep(1)
                                print("Idzie Ci dosyć ciężko...")
                                time.sleep(1)
                                print("Ostatkiem sił przechylasz rękę przeciwnika.")
                                time.sleep(1)
                                print("Pokonany!")
                                time.sleep(1)
                                print("Wszyscy w barze Ci gratulują")
                                time.sleep(1)
                                player.expAdd(5)
                                time.sleep(1)
                                player.moneyAdd(100)
                            else:
                                print("Walka trwa!")
                                time.sleep(1)
                                print("Idzie Ci bardzo ciężko")
                                time.sleep(1)
                                print("Przeciwnik jest wyraźnie silniejszy.")
                                time.sleep(1)
                                print("Przegrywasz...")
                        else:
                            print("Podchodzisz do stołu. Twój przeciwnik wydaje się być zdecydowanie od Ciebie większy...")
                            if player.strength > 80 or player.agility > 85:
                                print("Walka trwa!")
                                time.sleep(1)
                                print("Idzie Ci bardzo dobrze, ręka przeciwnika przechyla się w jego kierunku.")
                                time.sleep(1)
                                print("Jesteś coraz bliżej wygranej!")
                                time.sleep(1)
                                print("Pokonany!")
                                time.sleep(1)
                                print("Wszyscy w barze Ci gratulują")
                                time.sleep(1)
                                player.expAdd(10)
                            elif player.strength > 70 or player.agility > 75:
                                print("Walka trwa!")
                                time.sleep(1)
                                print("Idzie Ci dosyć ciężko...")
                                time.sleep(1)
                                print("Ostatkiem sił przechylasz rękę przeciwnika.")
                                time.sleep(1)
                                print("Pokonany!")
                                time.sleep(1)
                                print("Wszyscy w barze Ci gratulują")
                                time.sleep(1)
                                player.expAdd(5)
                            else:
                                print("Walka trwa!")
                                time.sleep(1)
                                print("Idzie Ci bardzo ciężko")
                                time.sleep(1)
                                print("Przeciwnik jest wyraźnie silniejszy.")
                                time.sleep(1)
                                print("Przegrywasz...")
                else:
                    print("Eosapiensy zapuszczają się ostatnio aż na rynek, nie słyszałeś?")
                    print("[1] Tak, wiem")
                    print("[2] Nie, o co chodzi?")
                    choice = input(">>")
                    if choice == "1":
                        print("Zobacz, Donald wygrał!")
                        print("[1] Chwila, co?")
                        print("[2] Brawo Donald!")
                        choice = input(">>")
                        if choice == "1":
                            print("Nie widzisz? Są zawody w siłowaniu się na rękę!")
                            print("Może weźmiesz udział?")

            #Jeśli gracz dostanie wiadomość
            elif player.ifGetMessage == 1:
                print("||| BAR |||")
                print("Przy jednym ze stolików widzisz swojego przyjaciela, podchodzisz do niego i wyjmujesz z kieszeni tajemniczy list.")
                print(">> Znasz się na szyfrach, możesz mi pomóc?")
                time.sleep(2)
                print("Jasne, pokaż mi co masz.")
                time.sleep(1)
                print(">> Podajesz list")
                print("Oho, z tego co widzę to stare, harcerskie szyfrowanie.")
                time.sleep(2)
                print("Nazywa się GA-DE-RY-PO-LU-KI")
                print("[1] Co to?")
                print("[2] Znam to!")
                answer = input(">>")
                if answer == 1:
                    print("Już Ci tłumaczę")
                    time.sleep(2)
                    print("Spójrz na ten ciąg liter: GA-DE-RY-PO-LU-KI")
                    time.sleep(2)
                    print("Jeśli chcesz zaszyfrować wiadomość to patrzysz na każdą kolejną literę.")
                    time.sleep(2)
                    print("Jeśli litera znajduje się w tym ciągu, to zamieniasz ją na drugą w parze.")
                    time.sleep(2)
                    print("Na przykład jeśli masz P, to szyfrujesz to jako O")
                    time.sleep(2)
                    print("Jeśli litery nie ma to ją zostawiasz.")
                    print("Rozumiesz?")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == 1:
                        decoding()
                    elif choice == 2:
                        print("To zakodujmy razem wyraz: KOT")
                        time.sleep(2)
                        print("Pierwsza litera K jest w parze z I")
                        time.sleep(1)
                        print("Druga litera O jest w parze z P")
                        time.sleep(1)
                        print("Ostatniej litery nie ma w ciągu, więc ją zostawiasz.")
                        time.sleep(1)
                        print("Zakodowany wyraz to więc IPT")
                        time.sleep(1)
                        print("Czas rozszyfrować Twoją wiadomość!")
                        decoding()
                else:
                    decoding()

        # Gracz idzie do mieszkania
        elif choice == "3":
            print("|||| MIESZKANIE |||")
            print("Otwierasz drzwi i widzisz, że na podłodze leży koperta.")
            print("Chyba jeszcze nigdy nie otrzymałeś papierowego listu.")
            print("Ostatnie wspomnienie jakie masz z listami to opowieści babci.")
            print("[1] Otwieram")
            print("[2] Robię kawę")
            choice = input(">>")
            if choice == "1":
                print("W kopercie znajduje się dziwny napis:")
                print('"Ipnkdc oydzredntg. Iygiów w podyzd. Oyzraptlj oyzdmpwę."')
                print("To chyba kod...")
                while True:
                    print("[1] Próbuję rozszyfrować")
                    print("[2] Ryszard zna się na szyfrach, lepiej go poszukam")
                    choice = input(">>")
                    if choice == "1":
                        letterInside = ("Kogjwu uuhkwui ssnejsp heuejim.", "Ghysisj Yhujis ujopmsshsia.", "Thsyuj ujaikjkp rygusm",
                                        "Thusnajokhsu hjkijaak iljpisujm.")
                        print("Chyba nikt by nie napisał")
                        print(random.choice(letterInside))
                        continue
                    else:
                        print("Wychodzisz z mieszkania. Idziesz szukać Ryszarda.")
                        player.ifGetMessage = 1
                        break
            else:
                print("Wchodzisz do kuchni. Włączasz ekspres do kawy. W oczekiwaniu na kawę włączasz grę w kółko i krzyżyk.")
                ### NAPISAĆ GRĘ W KÓŁKO I KRZYŻYK

        # Gracz idzie do sklepu
        elif choice == "5":
            shop()

        # Gracz wchodzi do ekwipunku
        elif choice == "6":
            look_in_inventory()

        #Gracz zapisuje grę
        elif choice == "7":
            save_game()

        #Gracz idzie na dworzec
        elif choice == "8":
            print("||| DWORZEC |||")
            print("Gdzie chcesz jechać?")
            if player.level == 2:
                print("[1] Do Krakowa")
            if player.level == 3:
                print("[2] Do Radomia")
            choice = input(">>")
            if choice == 1:
                krakow()
            elif choice == 2:
                radom()

def new_game():
    #Nowa gra
    global player
    print("Jakie wybierasz imię swojej postaci?")
    name = input(">>")
    player = character(name)
    warszawa()

def open_game():
    #Otwieranie zapisanej gry
    global player
    with open('gamesave1.pkl', 'rb') as input:
        player = pickle.load(input)
    if player.level == 1:
        warszawa()
    elif player.level == 2:
        krakow()
    elif player.level == 3:
        radom()
    return

def leaderboard():
    #Tablica wyników
    return

def save_game():
    global player
    with open('gamesave1.pkl', 'wb') as output:
        pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)


def game_help():
    #Pomoc w grze
    return
def tutorial():
    print("Witaj w grze Darwin4. Zanim zaczniesz grę, powinieneś poznać jedną, prostą zasadę:")
    time.sleep(1)
    print("Jeśli napotkasz moment, gdy będziesz musiał wybrać jedną z kilku opcji. Np. tak:")
    time.sleep(1)
    print("[1] Opcja pierwsza")
    print("[2] Opcja druga")
    time.sleep(1)
    print("Opcję, którą chcesz, wybierz przez wpisanie numeru:")
    print(">> 1")
    time.sleep(1)
    print("Może spróbujemy? Wybierz opcję pierwszą:")
    choice = input(">>")
    while True:
        if choice == "1":
            print("Brawo! Możesz już zacząć grę.")
            break
        else:
            print("Chyba coś nie wyszło... spróbuj jeszcze raz.")
            continue
    time.sleep(1)
    menu()
def menu():
    print("===MENU===")
    print("[1] Nowa gra")
    print("[2} Wczytaj grę")
    print("[3] Tablica wyników")
    print("[4] Pomoc")
    print("[5] Zakończ grę")
    print("Co chcesz zrobić?")
    menu_choice = input(">>")
    while True:
        if menu_choice in ("1", "[1]", "nowa", "nowa gra"):
            new_game()
            break
        elif menu_choice in ("2", "[2]", "wczytaj", "wczytaj gre", "wczytaj grę"):
            open_game()
            break
        elif menu_choice in ("3", "[3]", "tablica wyników", "tablica", "wynik", "wyniki"):
            leaderboard()
            break
        elif menu_choice in ("4", "[4]", "pomoc"):
            game_help()
            break
        elif menu_choice in ("5", "[5]", "zakończ", "koniec"):
            break
        else:
            continue

menu()

