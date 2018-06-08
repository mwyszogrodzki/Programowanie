
class postac(object):
    def __init__(self, name, mood):
        self.name = name
        self. mood = mood


    def attack(self):
        print("Tutaj następuje atak")

    def spotkanie(self, other):
        other.ucieczka()

class przeciwnik(postac):
    def __init__(self,  name, strength, charakter):
        self.charakter = charakter

    def ucieczka(self):
        if self.charakter == "zły":
            print(self.name, "ucieka")
        else:
            print("Spotkaliście się")


roman = postac("Roman", 50)
bogdan = przeciwnik("Bogdan", 50, "zły")

roman.spotkanie(bogdan)

