#Program tworzący klasę telewizora

class tele(object):
    def __init__(self,channel=1,loudness=30):
        self.channel=channel
        self.loudness=loudness
        print("Włączyłeś telewizor!")
        print("Obecny kanał ma numer:",channel,"\n Poziom głośności wynosi: ", loudness)

    def change_channel(self,new_channel):
        self.channel=new_channel
        print("Obecny kanał to:",self.channel)

    def change_loudness(self,new_loudness):
        self.loudness=new_loudness
        print("Obecna głośność to:",self.loudness)

    def status(self):
        print("Obecny kanał to:",self.channel,"\nPoziom głośności wynosi:",self.loudness)



def main():
    telewizor = tele()


    while True:
        print("""Co chcesz zrobić?
        0 - wyłącz telewizor
        1 - zmień kanał
        2 - zmień głośność
        3 - wyświetl status""")

        choice=int(input("Wybierz: "))

        if choice == 0:
            print("Wyłączyłeś")
            break
        elif choice == 1:
            new_channel = int(input("Podaj nowy kanał: "))
            if new_channel >= 0 and new_channel <= 20:
                telewizor.change_channel(new_channel)
            else:
                print("Masz tylko 20 kanałów :(")
            continue
        elif choice==2:
            new_loudness = int(input("Podaj nową głośność: "))
            if new_loudness >= 0 and new_loudness <= 100:
                telewizor.change_loudness(new_loudness)
            else:
                print("Głośność tylko w zakresie 0-100!")
            continue
        elif choice ==3:
            telewizor.status()
            continue
        else:
            print("Nie ma takiej opcji")
            continue

main()