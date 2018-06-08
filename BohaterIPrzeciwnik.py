import random

class bohater(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def obrona(self, attack_value):
        self.health -= attack_value
        print(self.name, "ma", self.health,"/100 punktów życia")

    def attack(self, enemy):
        attack_random = random.randint(1,20) + 5
        enemy.obrona(attack_random)

    def heal(self):
        self.health += random.randint(1,8)
        if self.health > 100:
            self.health = 100

class przeciwnik(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def obrona(self, attack_value):
        self.health -= attack_value
        print(self.name, "ma", self.health, "/100 punktów życia")

    def attack(self, enemy):
        attack_random = random.randint(1, 20) + 5
        enemy.obrona(attack_random)

bogdan = bohater("Bogdan")
stefan = przeciwnik("Stefan")

print("Spotkałeś przeciwnika! Walczysz czy uciekasz?")
print("[1] Walczę")
print("[2] Uciekam")
attack_choice = input(">>")
if attack_choice in ("1", "[2]", "walcze", "walczę", "walka"):
    while True:
        bogdan.attack(stefan)
        stefan.attack(bogdan)
        if bogdan.health <= 0:
            print("Przegrałeś")
            break
        elif stefan.health <= 0:
            print("Wygrałeś!")
            break
        bogdan.heal()
elif attack_choice in ("2", "[2]", "uciekam", "ucieczka"):
    lucky = random.randint(1,20)
    if lucky >= 3:
        print("Uciekłeś!")
    else:
        print("Przeciwnik Cię dogonił, musisz walczyć.")
        while True:
            bogdan.attack(stefan)
            stefan.attack(bogdan)
            if bogdan.health <= 0:
                print("Przegrałeś")
                break
            elif stefan.health <= 0:
                print("Wygrałeś!")
                break
            bogdan.heal()



