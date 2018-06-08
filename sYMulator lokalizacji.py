class lokacje(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def place(self):
        print("[ZNAJDUJESZ SIĘ W", self.name, "]")
        print(self.description)
        print("\n")

kuchnia = lokacje("Kuchnia", "Wszystkie szafki są otwarte, na stole leży zepsute jedzenie")
salon = lokacje("SALONIE", "Telewizor jest zniszczony, a kanapa podrapana. Czuć dziwny zapach,")
toaleta = lokacje("TOALECIE", "Wszystko zniszczone. Same kawałki.")
sypialnia = lokacje("SYPIALNI", "Na wielkim łóżku widać ślady krwii.")
magazynek = lokacje("MAGAZYNKU", "Wszystko opustoszało, ale widać jedną puszkę fasoli!")

def wybieranie():
    while True:
        print("Oto symulator lokacji.")
        print("""=========
kuchnia
salon
toaleta
sypialnia
magazynek
==========""")
        print("Wyjście - exit")
        print("Co wybierasz?")
        choice = input(">>")
        if choice == "kuchnia":
            kuchnia.place()
        elif choice == "salon":
            salon.place()
        elif choice == "toaleta":
            toaleta.place()
        elif choice == "sypialnia":
            sypialnia.place()
        elif choice == "magazynek":
            magazynek.place()
        elif choice == "exit":
            break
        else:
            print("Coś poszło nie tak. Spróbuj ponownie")

wybieranie()

