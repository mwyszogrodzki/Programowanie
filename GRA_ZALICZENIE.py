import random
import time
import pickle
import games

actions = { 'homeless' : "Rozmawiam z bezdomnym na rynku",
            'bar' : "Idę do baru",
            'home' : "Wracam do domu",
            'office' : "Idę do ratusza",
            'market' : "Idę na rynek",
            'shop' : "Idę do sklepu",
            'equip' : "Zaglądam do ekwipunku",
            'exit_hyperloop' : "Wychodzę z dworca",
            'party' : "Idę do siedziby partii",
            'hotel' : "Idę do hotelu",
            'park' : "Idę na planty",
            'park_radom' : "Idę do parku",
            'hyperloop' : "Idę na dworzec",
            'election' : "Idę na wybory",
            'event' : "Idę na ogłoszenie wyników",
            'shelter' : "Idę na akcję charytatywną",
            'opera' : "Idę do opery",
            'menu' : "Wyjdź do menu",
            'save' : "Zapisz grę"}

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
      "value": 10,
      "cost": 2000},
'5': {"name": "Szpon Eosapiensa",
      "type": 3,
      "value": 0,
      "cost": 1000},
'6' : {"name": "Kombinezon bezpieczeństwa",
       "type": 4,
       "value": 10,
       "cost": 3000},
'7' : {"name": "Koszula z kevlaru",
       "type": 4,
       "value": 5,
       "cost": 2000},
'8' : {"name": "Laserowy karabin snajperski",
       "type": 1,
       "value": 100,
       "cost": 5000},
'9': {"name": "Złota Puszka",
      "type": 3,
      "value": 0,
      "cost": 10000}}


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
        self.ifPlayerPlayedOnPhone = 0
        #Zmienić!!!!!!
        self.money = 500
        self.inventory = []
        self.possibleActions = ['homeless', 'bar', 'home', 'office', 'shop', 'save', 'menu']
        self.sebaAttaced = 0
        self.ifMetThief = 0
        self.elections = 0
        self.ifPlayerFightInBar = 0
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
        print("Stan konta:", self.money, "złotych")
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
        self.money -= value
        print("[STAN KONTA:", self.money, "ZŁ]")

    def moneyAdd(self, value):
        #Zwiększa stan konta
        self.money += value
        print("[STAN KONTA:", self.money, "ZŁ]")

    def inventoryAdd(self, item):
        self.inventory.append(item)
        print("""=== DO DWOJEGO EKWIPUNKU DODANO:""", things[item]["name"], "===")

    def inventoryRemove(self, item):
        self.inventory.remove(item)
        print("""=== Z TWOJEGO EKWIPUNKU USUNIĘTO:""", things[item]["name"],"===")

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
        attackWeapon = 0
        for i in self.inventory:
            if things[i]['type'] == 1:
                if things[i]['value'] > attackWeapon:
                    attackWeapon = things[i]['value']
        self.attackValue = self.strength*0.2 + self.agility*.1 + random.randint(1,10) + attackWeapon*0.4
        self.attackValue -= self.attackValue % 1
        print("## Atakujesz z siłą", self.attackValue,"##")
        enemy.defence(self.attackValue)

    def defence(self, attackValue):
        defenceWeapon = 0
        for i in self.inventory:
            if things[i]['type'] == 4:
                if things[i]['value'] > defenceWeapon:
                    attackWeapon = things[i]['value']

        self.defenceValue = attackValue - random.randint(1,5) - defenceWeapon*0.6
        self.health -= self.defenceValue
        if self.health > 100:
            self.health = 100
        print("## Pozostało Ci", self.health, "punktów życia. ##")

    def expAdd(self, value):
        self.exp += value

        print("+++ ZYSKAŁEŚ", value, "PUNKTÓW DOŚWIADCZENIA +++")
        if self.exp >= 100 * self.level:
            self.level += 1
            levelUp(self.level)
        print("+++   ", 100 * self.level - self.exp, "DO NASTĘPNEGO POZIOMU    +++")

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

def possibleAction(possibleActions):
    #Do funkcji jest przesyłana lista możliwych akcji, a funkcja zwraca wybraną akcję
    global actions
    while True:
        try:
            options = {}
            number = 1
            for i in possibleActions:
                options[number] = i
                number += 1
            print("Co robisz?")
            number = 1
            for i in options:
                print("[", number ,"]", actions[options[i]])
                number += 1
            choice = int(input(">>"))
            return options[choice]
        except ValueError:
            print("Wprowadziłeś złą wartość, spróbuj ponownie.")


def levelUp(level):
    if level == 2:
        player.possibleActions.append('hyperloop')
        print("BRAWO!")
        print("Awansowałeś! Masz już 2 poziom!")
    if level == 3:
        print("BRAWO!")
        print("Awansowałeś! Masz już 2 poziom!")

def endgame():
    print("Niestety poległeś... Planeta Darwin4 nie jest jednak tak przyjazna jak się wydawało.")
    menu()

def battle(enemy):
    winner = 0

    while True:
            if player.health > 0:
                player.attack(enemy)
            elif player.health < 0:
                print("Przegrałeś.")
                endgame()
                break
            if enemy.health > 0:
                enemy.attack()
            elif enemy.health <= 0:
                print("Wygrałeś!")
                winner += 1
                break
            if player.health <= 0:
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

def shop():
    #Funkcja wyświetla sklep
    print("||| SKLEP |||")
    #time.sleep(1)
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
            possibleItems = ('1', '2', '4', '6', '7')
            print("[0] Wróć")
            for i in possibleItems:
                print("[", i, "]", things[i]["name"], "| Cena:", things[i]["cost"])
            choice = input(">>")
            if choice == '0':
                continue
            if things[choice]['cost'] <= player.money:
                player.inventoryAdd(choice)
                player.moneyMinus(things[choice]['cost'])
            else:
                print("Masz za mało pieniędzy na ten przedmiot.")
                continue

        elif choice == '2':
            print("Który przedmiot?")
            print("[0] Wróć")
            for i in player.inventory:
                print("[", i, "]", things[i]["name"], "| Cena:", things[i]["cost"]*0.8)
            choice = input(">>")
            if choice == '0':
                continue
            player.inventoryRemove(choice)
            player.moneyAdd(things[choice]["cost"]*0.8)
            continue
        else:
            break

def radom():
    global player
    print("||| DWORZEC HYPERLOOP |||")
    print("Witaj w Radomiu! Twoja podróż była bardzo szybka")
    running = 1
    while True:
        try:
            while running == 0:
                player.possibleActions = ['market', 'park_radom', 'shelter', 'party', 'election', 'shop', 'hyperloop', 'save', 'menu']
                choice = possibleAction(player.possibleActions)

                #Gracz idzie na rynek
                if choice == "market":
                    print("||| RYNEK |||")
                    print("Wchodzisz na rynek, tłum zgromadził się już pod sceną. Czekają na Twoją przemowę.")
                    print("[1] Wchodzę na scenę")
                    print("[2] Robię sobie zdjęcia z ludźmi")
                    choice = input(">>")
                    if choice == "2":
                        print("Ludzie radośnie robią sobie z Tobą zdjęcia.")
                        player.elections += 3
                    print("[1] Drodzy zebrani, miło Was widzieć!")
                    print("[2] Witajcie w centrum tej planety!")
                    choice = input(">>")
                    if choice == '2':
                        player.elections += 3
                    print("[1] Darmowe loty kosmiczne dla każdego!")
                    print("[2] Większe podatki!")
                    choice = input(">>")
                    if choice == '1':
                        player.elections += 3
                    print("[1] Panuje tutaj za duża przestępczość! Sam już w swojej obronie zabiłem kilku złodziei.")
                    print("[2] To piękne miasto, ciche i spokojne.")
                    choice = input(">>")
                    if choice == '1':
                        player.elections += 3
                    print("Schodzisz z mównicy.")
                    time.sleep(1)
                    print("Podchodzi do Ciebie sekretarz partii:")
                    time.sleep(1)
                    print("Brawo! Masz juz", player.elections, "procent poparcia w kraju!")
                    player.expAdd(15)
                    time.sleep(1)
                    print("Nagle zauważasz, że obok Ciebie znajduje się kropka lasera.")
                    print("[1] Uciekam!")
                    print("[2] To pewnie zabawka")
                    choice = input(">>")
                    if choice == "2":
                        time.sleep(1)
                        print("Oj, to jednak był snajper.")
                        endgame()
                    meters = 100
                    while meters > 0:
                        meters -= player.agility + random.randint(1,15)
                        print("Pozostało Ci", meters, "metrów do bezpiecznego miejsca.")
                    print("Udało Ci się, uciekłeś! Lepiej odejdź stąd.")
                    player.expAdd(15)

                #Gracz idzie do parku
                elif choice == "park_radom":
                    print("||| PARK |||")
                    print("Widzisz grupkę podejrzanych osób w dresach, chyba mają ochotę na Twój telefon.")
                    names = ('Seba', 'Mati', 'Arek', 'Rafał', 'Przemek')
                    howManyEnemies = random.randint(1,5)
                    for i in range(0, howManyEnemies):
                        name = names[i]
                        name = mob(name, 50, 1)
                        battle(name)

                #Gracz idzie do siedziby partii
                elif choice == "party":
                    print(player.name, "czy chcesz wykupić reklamę w mediach?")
                    time.sleep(1)
                    print("To będzie kosztowało 2500zł")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == "1":
                        if player.money < 2500:
                            print("Niestety nie masz tylu pieniędzy.")
                        else:
                            player.moneyMinus(2500)
                            marketing = random.randint(1,10)
                            print("Udało się! Twoje poparcie wzrosło o", marketing, "procent")
                            player.elections += marketing
                            player.expAdd(5)
                    else:
                        print("Nie uważam tego za dobry pomysł, ale to Twoja decyzja.")
                    player.possibleActions.remove('party')

                #Gracz idzie na akcję charytatywną
                elif choice == "shelter":
                    print("||| AKCJA CHARYTATYWNA |||")
                    print("W parku stoi mnóstwo ludzi z psami oraz wolontariuszy.")
                    print("Podchodchodzi do Ciebie jedna z wolontariuszek:")
                    while True:
                        print('"Czy chciałby Pan wesprzeć naszą akcję? Chcemy otworzyć schronisko"')
                        print("[1] Nie ma mowy")
                        print("[2] Chętnie! Mogę też coś powiedzieć do zgromadzonych?")
                        print("[3] Oczywiście! Przeleję Wam 1000 złotych.")
                        choice = input(">>")
                        if choice == "1":
                            print("Dzwoni do Ciebie sekretarz:")
                            time.sleep(1)
                            player.elections -= 1
                            print('"Coś Ty zrobił?! Piesków nie wspierasz!? Spadło Ci poparcie do', player.elections, 'procent!"')
                            break
                        elif choice == "2":
                            print("Wchodzisz na mównicę i mówisz jak ważna jest dla Ciebie pomoc psom.")
                            time.sleep(1)
                            print("Dzwoni do Ciebie sekretarz:")
                            time.sleep(1)
                            player.elections += 4
                            print('"Nie wiem co robisz, ale robisz to dobrze. Wzrosło Ci poparcie do', player.elections, 'procent!"')
                            break
                        elif choice == "3":
                            player.elections += 2
                            player.moneyMinus(1000)
                            print("Zrobiłeś przelew.")
                            break
                        else:
                            continue

                #Gracz idzie na wybory
                elif choice == "election":
                    print("||| SALA WYBORÓW |||")
                    print("Przed salą stoi jakiś mężczyzna i nie chce Cię wpuścić")
                    print("Ciągle się tylko pyta:")
                    choice = ""
                    tries = 0
                    while choice.lower() != "tak:" or tries < 7:
                        print('"Czy da mi Pan autograf?"')
                        choice = input(">>")
                        tries += 1
                    print("Uff.. Udało Ci się przejść. Idziesz zagłosować")
                    player.possibleActions.append('event')

                elif choice == "event":
                    print("||| OGŁOSZENIE WYNIKÓW WYBORÓW |||")
                    print("Nadszedł ten wielki moment.")
                    time.sleep(1)
                    print("Już za chwilę zostaną ogłoszone wyniki wyborów!")
                    population = 100 - random.randint(1,9)
                    you = (election*1.5)/100 * population
                    you_int = you % 1
                    you -= you_int
                    left = population - you
                    firstCandidate = random.randrange(10, left - 5)
                    secondCandidate = 100 - you - firstCandidate

                    if you > firstCandidate:
                        if you > secondCandidate:
                            winner = 1
                        else:
                            winner = 3
                    else:
                        if firstCandidate > secondCandidate:
                            winner = 2
                        else:
                            winner = 3

                    time.sleep(2)
                    print("Trwa liczenie głosów.")
                    time.sleep(1)
                    print("Mamy zwycięzcę!")
                    time.sleep(1)
                    if winner == 1:
                        print("Wygrał...", player.name, "!!")
                        print("Cała sala Ci gratuluje!")
                    else:
                        print("Niestety nasz kandydat,", player.name, "przegrał.")
                        if winner == 2:
                            print("Prezydentem zostaje pierwszy kandydat")
                        else:
                            print("Prezydentem zostaje drugi kandydat")

                #Gracz idzie na dworzec:
                elif choice == 'hyperloop':
                    print("Gdzie chcesz jechać?")
                    print("[1] Do Warszawy")
                    print("[2] Do Krakowa")
                    choice = input(">>")
                    if choice == '1':
                        running = 0
                        warszawa()
                    elif choice == '2':
                        running = 0
                        krakow()

                #Zapisanie gry
                elif choice == "save":
                    print("Czy chcesz zapisać grę przed wyjściem?")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == "1":
                        save_game()
                        menu()
                    if choice == "2":
                        menu()

                #Wyjście do menu
                elif choice == "menu":
                    save_game()

                else:
                    radom()
        except ValueError:
            print("Wprowadziłeś złą wartość, spróbuj ponownie.")
        except:
            print("Wystąpił błąd. Spróbuj ponownie.")
def krakow():
    global player

    print("||| DWORZEC HYPERLOOP |||")
    print("Witaj w Krakowie! Twoja podróż była bardzo szybka")
    player.possibleActions = ['market', 'park', 'party', 'hotel', 'shop', 'hyperloop', 'save', 'menu']
    running = 1
    while True:
        try:
            while running:
                choice = possibleAction(player.possibleActions)
                #Gracz idzie na Planty
                if choice == "park":
                    print("||| PLANTY |||")
                    print("Idziesz zielonymi plantami dookoła centrum miasta.")
                    print("Widzisz stojącą maszynę z napisem LOTTO.")
                    print("Inny napis na urządzeniu informuje o możliwej wygranej nawet 20 tys złotych.")
                    print("[1] Podchodzę")
                    print("[2] Ignoruję")
                    choice = input(">>")
                    if choice == "1":
                        print("Podchodzisz do urządzenia, jedna gra kosztuje 10zł")
                        print("[1] Biorę udział")
                        print("[2] Odchodzę")
                        choice = input(">>")
                        if choice == "1":
                            player.moneyMinus(10)
                            won = games.lotto()
                            if won == 4:
                                player.moneyAdd(20000)
                            elif won == 3:
                                player.moneyAdd(2000)
                            elif won == 2:
                                player.moneyAdd(500)
                            elif won == 1:
                                player.moneyAdd(10)
                            player.expAdd(5)
                    if player.ifMetThief == 0:
                        print("Widzisz w oddali złodzieja, który odkradł staruszkę")
                        print("[1] Gonię go!")
                        print("[2] Ignoruję")
                        choice = input(">>")
                        metersToThief = 100
                        while metersToThief > 0:
                            obstacle = ('Nad ławką', 'Chodnik', 'Trawa', 'Między ludźmi', 'Przeskok nad psem', 'Przeskok nad płotkiem')
                            print("Jak biegniesz?")
                            print("[1]", random.choice(obstacle))
                            print("[2]", random.choice(obstacle))
                            choice = input(">>")
                            more = random.randint(1,2)
                            str(more)
                            if choice == '1':
                                if more == '1':
                                    metersToThief -= random.randint(5,20)
                                else:
                                    metersToThief -= random.randint(1,10)
                            else:
                                if more == '2':
                                    metersToThief -= random.randint(5,20)
                                else:
                                    metersToThief -= random.randint(1,10)
                            print("Pozostało", metersToThief, "m do złodzieja!")
                        thief = mob("Złodziej", 100, 1)
                        print("Dopadasz go, on jednak wyciąga broń")
                        if battle(thief):
                            player.expAdd(15)
                        player.ifMetThief = 1

                #Gracz idzie do siebiby partii
                elif choice == "party":
                    print("||| SIEDZIBA PARTII |||")
                    print('Chodź, czekaliśmy na Ciebie!')
                    print("Ochroniarz prowadzi Cię na aulę i wprowadza na scenę")
                    print("Stoisz na mównicy, przed Tobą cała sala działaczy partyjnych")
                    print("[1] Drodzy zebrani, miło Was widzieć!")
                    print("[2] Koniec tego! Nasz kraj musi przejść wielkie reformy!")
                    choice = input(">>")
                    if choice == '2':
                        player.elections += 1
                    print("[1] Musimy wprowadzić większe podatki!")
                    print("[2] W tym kraju rośnie przestępczość! Powinniśmy wprowadzić godzinę policyjną!")
                    choice = input(">>")
                    if choice == '1':
                        player.elections += 1
                    print("[1] To na pewno nie będzie łatwe")
                    print("[2] Oprócz tego musimy obniżyć pensję posłów!")
                    choice = input(">>")
                    if choice == '1':
                        player.elections += 1
                    print("[1] Obecny prezydent nigdy nie powinien wygrać!")
                    print("[2] Czas abym to ja był prezydentem!")
                    choice = input(">>")
                    if choice == '2':
                        player.elections += 1
                    print("[1] Pamiętajcie na kogo głosować!")
                    print("[2] Będę dumnie służył naszemu krajowi!")
                    choice = input(">>")
                    if choice == '1':
                        player.elections += 1
                    print("Schodzisz z mównicy.")
                    time.sleep(1)
                    print("Podchodzi do Ciebie sekretarz partii:")
                    time.sleep(1)
                    print("Brawo! Masz juz", player.elections, "procent poparcia w kraju!")
                    player.expAdd(15)
                    time.sleep(1)
                    print(player.name, "czy chcesz wykupić reklamę w mediach?")
                    time.sleep(1)
                    print("To będzie kosztowało 2500zł")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == "1":
                        if player.money < 2500:
                            print("Niestety nie masz tylu pieniędzy.")
                        else:
                            player.moneyMinus(2500)
                            marketing = random.randint(1,10)
                            print("Udało się! Twoje poparcie wzrosło o", marketing, "procent")
                            player.elections += marketing
                            player.expAdd(15)
                    else:
                        print("Nie uważam tego za dobry pomysł, ale to Twoja decyzja.")
                    player.possibleActions.remove('party')
                    player.possibleActions.append('opera')

                #Gracz idzie do opery, możliwe dopiero po wizycie w siedzibie partii
                elif choice == "opera":
                    print("||| OPERA |||")
                    print("Przed operą stoją tłumy ludzi.")
                    time.sleep(1)
                    print("Podbiega do Ciebie Rysiek i prosi abyś szedł za nim.")
                    time.sleep(1)
                    print('"Jak wiesz, trwa spotkanie z prezydentem, musimy się go pozbyć"')
                    time.sleep(1)
                    print("[1] Świetnie, daj mi tylko karabin.")
                    print("[2] Odwrócę uwagę strażników i idę do Ciebie")
                    choice = input(">>")
                    if choice == '1':
                        print("Poczekaj, najpierw musimy odwrócić uwagę strażników.")
                    time.sleep(1)
                    print("Podchodzisz do strażnika.")
                    print("[1] Jak leci na straży?")
                    print("[2] Wydaje mi się, że widziałem jakąś bójkę przy szatni, powinien Pan to chyba sprawdzić.")
                    choice = input(">>")
                    if choice == "1":
                        print("Dobrze, dobrze. Spokojny dzień.")
                        print("[1] To mam złe wieści, bo tam chyba zaczęła się jakaś bójka.")
                        print("[2] To mam złe wieści bo zaraz zabiję prezydenta.")
                        if choice == "1":
                            print("Dziękuję, już tam idę!")
                        elif choice == "2":
                            print("Strażnik Cię aresztuje. To był jednak błąd.")
                            endgame()
                    else:
                        print("Dziękuję, już tam idę!")
                    player.expAdd(10)
                    print("Szybko, musimy się dostać na balkon!")
                    rooms = {
                        1: {"name": "Korytarz",
                            "wschód": 2,
                            "południe": 3,
                            "północ": 5},
                        2: {"name": "Pokój sprzątaczek",
                            "zachód": 1,
                            "południe": 4},
                        3: {"name": "Schody",
                            "północ": 1},
                        4: {"name": "Zaplecze",
                            "północ": 2},
                        5: {"name": "Balkon",
                            "południe": 1}
                    }
                    currentRoom = 1
                    print("Użyj komendy:")
                    print("> idź [kierunek]")

                    while currentRoom != 5:
                        print("Jesteś w: " + rooms[currentRoom]["name"])
                        move = input("> ").lower().split()
                        if move[0] in ("idź", "idz"):
                            if move[1] in rooms[currentRoom]:
                                currentRoom = rooms[currentRoom][move[1]]
                            else:
                                print("Nie możesz tam iść!")
                    player.expAdd(10)
                    player.inventoryAdd('8')
                    president = mob("Prezydent", 200, 1)
                    print("Jesteś gotowy?")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == "2":
                        print("Chyba sobie żarty robisz, dawaj!")
                    toBeExposed = 10
                    while president.health > 0:
                        player.attack(president)
                        toBeExposed -= 1
                    if toBeExposed > 0:
                        print("Udało się! Uciekamy! Biegnij na dworzec!")
                        player.expAdd(20)
                    else:
                        print("To chyba koniec, zobacz, biegną po nas!")
                        endgame()

                #Gracz idzie na rynek
                elif choice == "market":
                    print(player.sebaAttaced)
                    if player.sebaAttaced == 0:
                        print("||| ULICA PROWADZĄCA DO RYNKU |||")
                        print("Uliczka wydaje Ci się lekko niepokojąca, jest raczej pusta, a lokale obskurne.")
                        print("Nagle ktoś podbiega do Ciebie i wyciąga nóż")
                        print('"Dawaj kasę!"')
                        print("[1] Oddaję mu całe pieniądze")
                        print("[2] Walczę")
                        print("[3] Uciekam")
                        seba = mob("Seba", 100, 2)
                        choice = input(">>")
                        if choice == "1":
                            player.moneyMinus(player.money)
                        elif choice == "2":
                            if battle(seba):
                                player.expAdd(15)
                        else:
                            if player.agility > 65:
                                print("Udało Ci się uciec!")
                            else:
                                print("Dopadł Cię!")
                                if battle(seba):
                                    player.expAdd(15)
                    print("||| RYNEK |||")
                    print("Pierwszy raz jesteś w Krakowie. Rozglądasz się po rynku i odkrywasz, że jest dokładnie")
                    print("taki sam jak na zdjęciach z ziemi.")
                    time.sleep(1)
                    print("Jeszcze większe zaskoczenie Cię spotyka kiedy podchodzi do Ciebie ten sam bezdomny co w Warszawie.")
                    print('"Kierowniku!"')
                    print("[1] Parę dni temu w Warszawie, a teraz w Krakowie?")
                    print("[2] Nie dam Ci już ani grosza.")
                    choice = input(">>")
                    if choice == "1":
                        print('"Mam już dosyć tych potworów, to się tutaj przeprowadziłem.')
                        print("[1] I jest już spokojniej?")
                        print("[2] Za moje pieniądze...")
                        choice = input(">>")
                        if choice == "1":
                            print('"Tak, ale zginął mi gdzieś Czerwony Talizman... Ile ja bym dał, żeby go odzyskać"')
                            print("[1] Chyba go znalazłem.")
                            print("[2] Wybacz, nie wiem o czym mówisz.")
                            choice = input(">>")
                            if choice == '1':
                                if player.checkInventory('3'):
                                    player.inventoryRemove('3')
                                    print('"Kierowniku kochany! Mogę dać w zamian tylko taką puszkę, może na coś się przyda..."')
                                    player.inventoryAdd('9')
                                    player.expAdd(10)
                                    print("Puszka wydaje się być nietypowa, może lepiej sprawdzić w sklepie ile jest warta.")
                                else:
                                    print("Nie, niestety to nie to...")
                            else:
                                print("A idź Pan stąd!")
                    else:
                        print("A idź Pan stąd!")
                    player.possibleActions.remove('market')

                #Gracz idzie do hotelu
                elif choice == "hotel":
                    print("||| POKÓJ HOTELOWY |||")
                    print("[1] Siadasz na łóżku i wyciągasz telefonie")
                    choice = input(">>")
                    if choice == "1":
                        print("Zaczynasz grę w zgadywanie na telefonie.")
                        if games.guessing():
                            player.expAdd(15)
                    print("Orientujesz się, że zatrzasnąłeś się w pokoju.")
                    print("Musisz znaleźć coś co może posłużyć za wytrych.")
                    while True:
                        placeInHotel = ('Pod łóżkiem', 'W komodzie', 'Za obrazem', 'Pod telewizorem', 'W łazience', 'W kuchni', 'W szafie')
                        firstPlace = random.choice(placeInHotel)
                        secondPlace = random.choice(placeInHotel)
                        if secondPlace == firstPlace:
                            continue
                        print("Gdzie szukasz?")
                        print("[1]", firstPlace)
                        print("[2]", secondPlace)
                        choice = input(">>")
                        if choice == '1':
                            if firstPlace == "W szafie":
                                print("Znalazłeś! Możesz wyjść!")
                                player.expAdd(15)
                                break
                            else:
                                print("Nie, to nie to...")
                                continue
                        elif choice == '2':
                            if secondPlace == "W szafie":
                                print("Znalazłeś! Możesz wyjść!")
                                player.expAdd(15)
                                break
                            else:
                                print("Nie, to nie to...")
                                continue

                #Gracz wchodzi do sklepu
                elif choice == "shop":
                    shop()

                #Gracz idzie na dworzec:
                elif choice == 'hyperloop':
                    print("Gdzie chcesz jechać?")
                    print("[1] Do Warszawy")
                    if player.level >= 3:
                        print("[2] Do Radomia")
                    choice = input(">>")
                    if choice == '1':
                        running = 0
                        warszawa()
                    elif choice == '2':
                        if player.level == 2:
                            print("Masz za niski poziom.")
                        else:
                            running = 0
                            radom()

                #Zapisanie gry
                elif choice == "menu":
                    print("Czy chcesz zapisać grę przed wyjściem?")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == "1":
                        save_game()
                        menu()
                    if choice == "2":
                        menu()

                #Wyjście do menu
                elif choice == "save":
                    save_game()
        except ValueError:
            print("Wprowadziłeś złą wartość, spróbuj ponownie.")
        except:
            print("Wystąpił błąd. Spróbuj ponownie.")

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
        try:
            while True:
                if player.ifTalkedWithHomeless:
                    actions['homeless'] = "Idziesz na rynek"

                choice = possibleAction(player.possibleActions)
                # Gracz idzie na rynek
                if choice == "homeless":
                    #Jeśli gracz nie rozmawiał z bezdomnym to nie pojawią się potwory
                    if player.ifTalkedWithHomeless == 0:
                        print("[BEZDOMNY] Kierownik nie boi się tak samemu tu spacerować?")
                        print("[1] Niby dlaczego?")
                        print("[2] W tym mieście niczego się nie boję!")
                        choice = input(">>")
                        if choice == "1":
                            print("Ostatnio w naszym mieście jest niebezpiecznie.")
                            print("Bo jest jest jeszcze taka sprawa...")
                            print("Złotóweczki mi brakuje do gwiezdnych pierogów.")
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
                                    player.expAdd(5)
                            else:
                                print("Odszedłeś.")
                        elif choice == "2":
                            print("Jeszcze zobaczysz jak bardzo się mylisz...")
                        continue
                    #Za to pojawią się jeśli rozmawiał
                    else:
                        #Program losuje czy pojawi się eosapiens
                        random_binary = random.randint(0,3)
                        if random_binary != 1:
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
                                        player.expAdd(18)
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
                elif choice == 'office':
                    if player.ifTalkedWithGrazynka == 0:
                        print("||| RATUSZ |||")
                        time.sleep(1)
                        print("Wchodzisz do urzędu, w środku jest prawie pusto. Jedna kobieta rozmawia z robotem w okienku.")
                        time.sleep(1)
                        print("Na wielkich ekranach wyświetla się ogłoszenie o nagrodzie za zabicie eosapiensów na rynku.")
                        time.sleep(1)
                        print("Znajdujesz jedynego człowieka z urzędu z którym możesz porozmawiać.")
                        time.sleep(1)
                        print("Kobieta z krótkimi włosami w średnim wieku, siedzi za okienkiem popijając kawę i rozwiązując krzyżówki na swoim tablecie.")
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
                        print('Mówisz: "Widziałem, że jest ustalona nagroda za zabicie eosapiensów. Mogę dostać więcej szczegółów?"')
                        time.sleep(1)
                        print(
                            '"Kochaniutki, to proste, zabij 3 z nich na rynku i prznieś mi po jednym szponie od każdego. Nagroda to 5 tysięcy"')
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
                                player.inventoryRemove('5')
                                player.inventoryRemove('5')
                                player.inventoryRemove('5')
                                player.moneyAdd(5000)
                                player.expAdd(25)
                                player.ifTalkedWithGrazynka = 900
                        print("Odchodzisz.")

                # Gracz idzie do baru
                elif choice == 'bar':
                    #Jeśli gracz nie dostanie wiadomości
                    if player.ifGetMessage in (0, 2):
                        print("||| BAR |||")
                        time.sleep(1)
                        print("Wchodzisz do swojego ulubionego baru. Jest trochę obskurny, ale mają najlepsze ceny.")
                        time.sleep(1)
                        if player.ifPlayerFightInBar == 0:
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
                                    player.ifPlayerFightInBar = 1
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
                                if choice == "2":
                                    print("No ciągle chodzą aż na rynek, ktoś powinien w końcu coś z tym zrobić!")
                        else:
                            print("Tym razem jest spokojnie, zamawiasz piwo?")
                            print("[1] Tak")
                            print("[2] Nie")
                            choice = input(">>")
                            if choice == "1":
                                player.moneyMinus(5)
                                player.healthPlus(5)
                            else:
                                print("Wychodzisz")
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
                        choice = input(">>")
                        if choice == str(1):
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
                            if choice == "1":
                                games.decoding()
                                player.expAdd(20)
                            elif choice == "2":
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
                                games.decoding()
                                player.expAdd(20)
                        else:
                            games.decoding()
                            player.expAdd(20)
                        player.ifGetMessage += 1

                # Gracz idzie do mieszkania
                elif choice == "home":
                    print("|||| MIESZKANIE |||")
                    if player.ifGetMessage == 0:
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
                            if player.ifPlayerPlayedOnPhone == 0:
                                print("Wchodzisz do kuchni. Włączasz ekspres do kawy. W oczekiwaniu na kawę włączasz grę w skojarzenia.")
                                player.expAdd(games.associations())
                                player.ifPlayerPlayedOnPhone = 1
                            else:
                                print("Wchodzisz do kuchni. Robisz sobie kawę.")
                    else:
                        if player.ifPlayerPlayedOnPhone == 0:
                            print("Wchodzisz do mieszkania i siadasz na łóżku.")
                            print("[1] Wyciągam telefon")
                            print("[2] Wychodzę")
                            choice = input(">>")
                            if choice == '1':
                                player.expAdd(games.associations())
                        else:
                            print("Cisza, pusto, nudy. Wracasz na rynek.")

                # Gracz idzie do sklepu
                elif choice == "shop":
                    shop()

                # Gracz wchodzi do ekwipunku
                elif choice == "equip":
                    look_in_inventory()

                #Gracz zapisuje grę
                elif choice == "save":
                    save_game()

                #Wyjście do menu
                elif choice == "menu":
                    print("Czy chcesz zapisać grę przed wyjściem?")
                    print("[1] Tak")
                    print("[2] Nie")
                    choice = input(">>")
                    if choice == "1":
                        save_game()
                        menu()
                    if choice == "2":
                        menu()

                #Gracz idzie na dworzec
                elif choice == "hyperloop":
                    print("||| DWORZEC |||")
                    print("Gdzie chcesz jechać?")
                    if player.level >= 2:
                        print("[1] Do Krakowa")
                    if player.level >= 3:
                        print("[2] Do Radomia")
                    choice = input(">>")
                    if choice == '1':
                        krakow()
                        break
                    elif choice == '2':
                        radom()
                        break
                else:
                    continue
        except ValueError:
            print("Wprowadziłeś złą wartość, spróbuj ponownie.")
        except:
            print("Wystąpił błąd. Spróbuj ponownie.")

def new_game():
    #Nowa gra
    global player
    print("Jakie wybierasz imię swojej postaci?")
    name = input(">>")
    player = character(name)
    warszawa()
    return

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
    print("/// GRA ZOSTAŁA ZAPISANA ///")


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
    while True:
        print("Może spróbujemy? Wybierz opcję pierwszą:")
        choice = input(">>")
        if choice == "1":
            print("Brawo! Możesz już zacząć grę.")
            break
        else:
            print("Chyba coś nie wyszło... spróbuj jeszcze raz.")
            continue
    time.sleep(1)
    menu()

def menu():
    while True:
        try:
            print("===MENU===")
            print("[1] Nowa gra")
            print("[2] Wczytaj grę")
            print("[3] Tablica wyników")
            print("[4] Pomoc")
            print("[5] Zakończ grę")
            print("Co chcesz zrobić?")
            menu_choice = input(">>")
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
        except FileNotFoundError:
            print("Nie masz zapisanej żadnej gry.")

tutorial()
