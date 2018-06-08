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

possibleActions = (1, 2, 3, 4, 6, 7, 99)

